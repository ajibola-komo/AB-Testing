from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

SQL_DIR = PROJECT_ROOT / "sql"

DBT_DIR = PROJECT_ROOT / "ab_testing"


SNOWFLAKE_AB_TEST = SQL_DIR / "ab_test.sql"
SNOWFLAKE_COUNTRIES = SQL_DIR / "countries.sql"
SNOWFLAKE_STATISTISTICAL_SUMMARY = SQL_DIR / "statistical_analysis.sql"

SNOWFLAKE_TABLE_NAMES = ["ab_test", "countries"]

