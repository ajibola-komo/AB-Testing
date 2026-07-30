from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DDL_DIR = PROJECT_ROOT / "ddl"
RAW_DIR = PROJECT_ROOT / "raw"

DB_DIR = PROJECT_ROOT / "ab_testing.db"
DBT_DIR = PROJECT_ROOT / "ab_testing"

DDL_AB_TEST = DDL_DIR / "sql" / "ab_test.sql"
DDL_COUNTRIES = DDL_DIR / "sql" / "countries.sql"

SNOWFLAKE_AB_TEST = DDL_DIR / "snowflake" / "ab_test.sql"
SNOWFLAKE_COUNTRIES = DDL_DIR / "snowflake" / "countries.sql"
SNOWFLAKE_STATISTISTICAL_SUMMARY = DDL_DIR / "snowflake" / "statistical_analysis.sql"

RAW_AB_TEST = RAW_DIR / "ab_test.csv"
RAW_COUNTRIES = RAW_DIR / "countries_ab.csv"

SNOWFLAKE_TABLE_NAMES = ["ab_test", "countries"]

