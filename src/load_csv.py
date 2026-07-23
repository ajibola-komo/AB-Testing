import pandas as pd
import numpy as np
import duckdb as db
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
from dotenv import load_dotenv
from src.config.envariables import SNOWFLAKE_CONFIG

from src.config.paths import (DDL_AB_TEST, DDL_COUNTRIES, SNOWFLAKE_AB_TEST, SNOWFLAKE_COUNTRIES, RAW_AB_TEST, RAW_COUNTRIES, DB_DIR,
                              SNOWFLAKE_TABLE_NAMES
                              )

load_dotenv()

def load_csv_data(conn):
        create_db1 = DDL_AB_TEST.read_text()
        create_db2 = DDL_COUNTRIES.read_text()

        conn.execute(create_db1)
        conn.execute(create_db2)

        conn.execute(f'''
        insert into ab_test (id, event_time, con_treat, page, converted) SELECT id, event_time, con_treat, page, converted from read_csv_auto('{RAW_AB_TEST}')

''')

        conn.execute(f'''
        INSERT INTO countries select * from read_csv_auto('{RAW_COUNTRIES}')
    ''')

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

def load_to_snowflake(conn):

    connect = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    cursor = connect.cursor()

    cursor.execute("DROP TABLE IF EXISTS ab_test")
    cursor.execute("DROP TABLE IF EXISTS countries")

    create_snowflake_tables()

    ab_test = conn.execute('''SELECT id, event_time, con_treat, page, converted FROM ab_test''').df()
    countries = conn.execute('''SELECT id, country FROM countries''').df()

    cursor.execute(f"USE DATABASE {SNOWFLAKE_CONFIG.get('database')}")
    cursor.execute(f"USE SCHEMA {SNOWFLAKE_CONFIG.get('database')}.{SNOWFLAKE_CONFIG.get('schema')}")
    cursor.execute(f"USE WAREHOUSE {SNOWFLAKE_CONFIG.get('warehouse')}")
    #cursor.executemany('INSERT INTO ab_test (id, event_time, con_treat, page, converted) VALUES (%s, %s, %s, %s, %s)', ab_test.itertuples(index=False, name=None))
    #cursor.executemany('INSERT INTO countries (id,country) VALUES (%s, %s)', countries.itertuples(index=False, name=None))

    
    write_pandas(connect, ab_test, 'AB_TEST', quote_identifiers=False)
    write_pandas(connect, countries, 'COUNTRIES', quote_identifiers=False)

    cursor.close()
    connect.close()



def main():
    conn = db.connect(DB_DIR)
    load_csv_data(conn)
    load_to_snowflake(conn)
    conn.close()

main()
