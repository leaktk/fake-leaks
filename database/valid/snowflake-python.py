# Metadata: label=Snowflake connection strings in Python, type=database_connection, db_type=snowflake, context=Python code, generator=manual

import snowflake.connector
from snowflake.connector import DictCursor
import os

class SnowflakeConfig:
    # Standard Snowflake connection parameters
    ACCOUNT = "xy12345.us-east-1"
    USER = "analytics_user"
    PASSWORD = "Sn0wfl@ke_P@ssw0rd_2026!"
    WAREHOUSE = "COMPUTE_WH"
    DATABASE = "ANALYTICS_DB"
    SCHEMA = "PUBLIC"
    ROLE = "ANALYST_ROLE"

    # Connection with all parameters
    FULL_CONNECTION_STRING = "snowflake://analytics_user:Sn0wfl@ke_P@ssw0rd_2026!@xy12345.us-east-1/ANALYTICS_DB/PUBLIC?warehouse=COMPUTE_WH&role=ANALYST_ROLE"

    # Alternative account formats
    ACCOUNT_AWS = "ab12345.us-west-2.aws"
    ACCOUNT_AZURE = "cd67890.east-us-2.azure"
    ACCOUNT_GCP = "ef24680.us-central1.gcp"

def get_snowflake_connection():
    """Create Snowflake connection using connector"""
    conn = snowflake.connector.connect(
        user='data_engineer',
        password='D@t@_Eng1n33r_Sn0wfl@ke!',
        account='xy12345.us-east-1',
        warehouse='ETL_WH',
        database='RAW_DATA',
        schema='STAGING',
        role='DATA_ENGINEER'
    )
    return conn

def get_connection_with_key_pair():
    """Snowflake connection with private key authentication"""
    conn = snowflake.connector.connect(
        user='service_account',
        account='xy12345.us-east-1',
        private_key_file='/path/to/rsa_key.p8',
        private_key_file_pwd='K3y_P@ssw0rd_2026!',
        warehouse='SERVICE_WH',
        database='PROD_DB',
        schema='PUBLIC',
        role='SERVICE_ROLE'
    )
    return conn

# Environment-based configuration
SNOWFLAKE_ENV_CONFIG = {
    'account': os.getenv('SNOWFLAKE_ACCOUNT', 'xy12345.us-east-1'),
    'user': os.getenv('SNOWFLAKE_USER', 'admin_user'),
    'password': os.getenv('SNOWFLAKE_PASSWORD', 'Adm1n_Sn0wfl@ke_P@ss!'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE', 'ADMIN_WH'),
    'database': os.getenv('SNOWFLAKE_DATABASE', 'ADMIN_DB'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA', 'PUBLIC'),
    'role': os.getenv('SNOWFLAKE_ROLE', 'ACCOUNTADMIN')
}

# SSO/OAuth connection
def get_sso_connection():
    """Snowflake connection with OAuth token"""
    conn = snowflake.connector.connect(
        user='sso_user@example.com',
        account='xy12345.us-east-1',
        authenticator='oauth',
        token='5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a',
        warehouse='SSO_WH',
        database='SSO_DB'
    )
    return conn

# External browser authentication
EXTERNAL_BROWSER_CONFIG = {
    'account': 'xy12345.us-east-1',
    'user': 'federated_user@company.com',
    'authenticator': 'externalbrowser',
    'warehouse': 'FEDERATED_WH',
    'database': 'ANALYTICS_DB'
}

# JDBC connection string format
JDBC_CONNECTION = "jdbc:snowflake://xy12345.us-east-1.snowflakecomputing.com/?user=jdbc_user&password=JDBC_P@ssw0rd_2026!&db=JDBC_DATABASE&schema=PUBLIC&warehouse=JDBC_WH&role=JDBC_ROLE"

# SQLAlchemy connection string
SQLALCHEMY_URL = "snowflake://sqlalchemy_user:SQL@lchemy_P@ss_2026!@xy12345.us-east-1/SQLALCHEMY_DB/PUBLIC?warehouse=SQLALCHEMY_WH&role=TRANSFORMER"
