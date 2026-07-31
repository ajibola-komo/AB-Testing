import pandas as pd
import numpy as np
import duckdb as db
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
from dotenv import load_dotenv
from src.config.envariables import SNOWFLAKE_CONFIG
import subprocess
from src.statistical_analysis import run_statistical_analysis

from src.config.paths import (SNOWFLAKE_AB_TEST, SNOWFLAKE_COUNTRIES,DBT_DIR)

load_dotenv()

def create_snowflake_tables():

    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    cursor = conn.cursor()
    

    database_name = SNOWFLAKE_CONFIG.get("database")
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")


    schema_name = SNOWFLAKE_CONFIG.get("schema")
    cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {database_name}.{schema_name}")

    cursor.execute(f"USE DATABASE {database_name}")
    cursor.execute(f"USE SCHEMA {database_name}.{schema_name}")

    SNOWFLAKE_DDL_PATHS = [SNOWFLAKE_AB_TEST, SNOWFLAKE_COUNTRIES]

    for ddl_path in SNOWFLAKE_DDL_PATHS:
        try:
            print(f"Running: {ddl_path}")

            with open(ddl_path, "r") as f:
                ddl = f.read()

                cursor.execute(ddl)

            print(f"SUCCESS: {ddl_path}")

        except Exception as e:
            print(f"FAILED: {ddl_path}")
            print(e)
            raise

    cursor.close()
    conn.close()

def load_to_snowflake():

    connect = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    cursor = connect.cursor()

    cursor.execute("DROP TABLE IF EXISTS ab_test")
    cursor.execute("DROP TABLE IF EXISTS countries")

    create_snowflake_tables()

    ab_test = pd.read_csv('raw/ab_test.csv',delimiter=',')
    countries = pd.read_csv('raw/countries_ab.csv',delimiter=',')

    cursor.execute(f"USE DATABASE {SNOWFLAKE_CONFIG.get('database')}")
    cursor.execute(f"USE SCHEMA {SNOWFLAKE_CONFIG.get('database')}.{SNOWFLAKE_CONFIG.get('schema')}")
    cursor.execute(f"USE WAREHOUSE {SNOWFLAKE_CONFIG.get('warehouse')}")
    #cursor.executemany('INSERT INTO ab_test (id, event_time, con_treat, page, converted) VALUES (%s, %s, %s, %s, %s)', ab_test.itertuples(index=False, name=None))
    #cursor.executemany('INSERT INTO countries (id,country) VALUES (%s, %s)', countries.itertuples(index=False, name=None))

    
    write_pandas(connect, ab_test, 'AB_TEST', quote_identifiers=False)
    write_pandas(connect, countries, 'COUNTRIES', quote_identifiers=False)

    cursor.close()
    connect.close()

def run_dbt():

    subprocess.run(
    [
        "dbt",
        "run",
        "--project-dir", 
        DBT_DIR
    ],
    check=True
)

def main():
    load_to_snowflake()
    run_statistical_analysis()
    run_dbt()
