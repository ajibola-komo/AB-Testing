import duckdb as db
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
from dotenv import load_dotenv
from src.config.envariables import SNOWFLAKE_STATISTICS_CONFIG
from src.config.paths import SNOWFLAKE_STATISTISTICAL_SUMMARY
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.proportion import confint_proportions_2indep

load_dotenv()

def run_statistical_analysis():

    connect = snowflake.connector.connect(**SNOWFLAKE_STATISTICS_CONFIG)
    cursor = connect.cursor()

    cursor.execute(f"USE DATABASE {SNOWFLAKE_STATISTICS_CONFIG.get('database')}")
    cursor.execute(f"USE SCHEMA {SNOWFLAKE_STATISTICS_CONFIG.get('database')}.{SNOWFLAKE_STATISTICS_CONFIG.get('schema')}")
    cursor.execute(f"USE WAREHOUSE {SNOWFLAKE_STATISTICS_CONFIG.get('warehouse')}")

    print("here 1")
    try:
        with open(SNOWFLAKE_STATISTISTICAL_SUMMARY,"r") as f:
            ddl = f.read()

            cursor.execute(ddl)
    except Exception as e:
        print("Cannot run")
        raise

        print("here 2")
    df1 = cursor.execute('''
        with get_top_metrics as (
        select
            count(case when test_group = 'control' and test_page = 'old_page' then user_id end ) as control_sessions,
            count(case when test_group = 'treatment' and test_page = 'new_page' then user_id end) as treatment_sessions,
            count(case when test_group = 'control' and test_page = 'old_page' and is_converted = 1 then user_id end) as control_conversions,
            count(case when test_group = 'treatment' and test_page = 'new_page' and is_converted = 1 then user_id end) as treatment_conversions,
            count(*) as total_sessions
            from mart_ab_test
        ), second_level_metrics as(
        select total_sessions,
        control_sessions, control_conversions, treatment_conversions, 
        treatment_sessions, (control_conversions::FLOAT / nullif(control_sessions,0)) as control_conversion_rate,
        (treatment_conversions::FLOAT / nullif(treatment_sessions,0)) as treatment_conversion_rate
        from get_top_metrics
        ) select total_sessions, control_sessions, treatment_sessions, control_conversions, treatment_conversions, 
        control_conversion_rate, treatment_conversion_rate, 
        (treatment_conversion_rate - control_conversion_rate)::FLOAT / nullif(control_conversion_rate,0) as relative_lift,
        (treatment_conversion_rate - control_conversion_rate) as absolute_lift
    from second_level_metrics
''').fetch_pandas_all()

    df1.columns = df1.columns.str.lower()

    metrics = df1.iloc[0]

    control_sessions = metrics["control_sessions"]
    treatment_sessions = metrics["treatment_sessions"]

    control_conversions = metrics["control_conversions"]
    treatment_conversions = metrics["treatment_conversions"]

    count = [
    treatment_conversions,
    control_conversions
    ]

    nobs = [
    treatment_sessions,
    control_sessions
    ]

    z_stat, p_value = proportions_ztest(count,nobs)

    ci_low, ci_high = confint_proportions_2indep(treatment_conversions,treatment_sessions,control_conversions,control_sessions)

    df2 = pd.DataFrame({
        'total_control_sessions':control_sessions,
        'total_treatment_sessions':treatment_sessions,
        'control_conversion_rate':df1['control_conversion_rate'],
        'treatment_conversion_rate':df1['treatment_conversion_rate'],
        'absolute_lift':df1['absolute_lift'],
        'relative_lift':df1['relative_lift'],
        'z_statistic': z_stat,
        'p_value':p_value,
        'ci_lower': ci_low,
        'ci_upper': ci_high ,
        'is_significant': p_value < 0.05
    })

    write_pandas(connect, df2, 'mart_statistical_summary', overwrite=True, quote_identifiers=False)


    cursor.close()
    connect.close()

    
