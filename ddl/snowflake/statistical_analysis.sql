CREATE OR REPLACE TABLE mart_statistical_summary(
    control_sessions bigint,
    treatment_sessions bigint,
    control_conversion_rate decimal(5,2),
    treatment_conversion_rate decimal(5,2),
    absolute_lift decimal(5,2),
    relative_lift decimal(5,2),
    z_statistic decimal(5,2),
    p_value decimal(5,2),
    ci_lower decimal(5,2),
    ci_upper decimal(5,2)
)