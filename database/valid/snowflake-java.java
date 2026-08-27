// Metadata: label=Snowflake JDBC connection in Java, type=database_connection, db_type=snowflake, context=Java code, generator=manual

package com.example.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class SnowflakeConnectionManager {

    // JDBC connection string
    private static final String SNOWFLAKE_URL =
        "jdbc:snowflake://xy12345.us-east-1.snowflakecomputing.com/";

    private static final String SNOWFLAKE_USER = "java_app_user";
    private static final String SNOWFLAKE_PASSWORD = "J@v@_Sn0wfl@ke_P@ss_2026!";
    private static final String SNOWFLAKE_WAREHOUSE = "JAVA_WH";
    private static final String SNOWFLAKE_DATABASE = "JAVA_DB";
    private static final String SNOWFLAKE_SCHEMA = "PUBLIC";
    private static final String SNOWFLAKE_ROLE = "JAVA_APP_ROLE";

    /**
     * Create Snowflake connection with basic authentication
     */
    public static Connection getConnection() throws SQLException {
        Properties props = new Properties();
        props.put("user", SNOWFLAKE_USER);
        props.put("password", SNOWFLAKE_PASSWORD);
        props.put("warehouse", SNOWFLAKE_WAREHOUSE);
        props.put("db", SNOWFLAKE_DATABASE);
        props.put("schema", SNOWFLAKE_SCHEMA);
        props.put("role", SNOWFLAKE_ROLE);

        return DriverManager.getConnection(SNOWFLAKE_URL, props);
    }

    /**
     * Create connection with inline credentials
     */
    public static Connection getConnectionInline() throws SQLException {
        String url = "jdbc:snowflake://xy12345.us-east-1.snowflakecomputing.com/?" +
                     "user=inline_user&" +
                     "password=Inl1n3_Sn0wfl@ke_P@ss!&" +
                     "db=INLINE_DATABASE&" +
                     "warehouse=INLINE_WH&" +
                     "schema=PUBLIC&" +
                     "role=INLINE_ROLE";

        return DriverManager.getConnection(url);
    }

    /**
     * Create connection with OAuth token
     */
    public static Connection getOAuthConnection() throws SQLException {
        Properties props = new Properties();
        props.put("user", "oauth_java_user@example.com");
        props.put("authenticator", "oauth");
        props.put("token", "3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a");
        props.put("warehouse", "OAUTH_JAVA_WH");
        props.put("db", "OAUTH_DB");
        props.put("schema", "PUBLIC");

        return DriverManager.getConnection(SNOWFLAKE_URL, props);
    }

    /**
     * Create connection with key-pair authentication
     */
    public static Connection getKeyPairConnection() throws SQLException {
        Properties props = new Properties();
        props.put("user", "keypair_java_user");
        props.put("privateKeyFile", "/app/secrets/snowflake_rsa.p8");
        props.put("privateKeyFilePwd", "K3yP@ir_J@v@_P@ss_2026!");
        props.put("warehouse", "KEYPAIR_WH");
        props.put("db", "SECURE_DATABASE");
        props.put("schema", "PROTECTED");
        props.put("role", "KEYPAIR_ROLE");

        return DriverManager.getConnection(SNOWFLAKE_URL, props);
    }

    /**
     * Production configuration
     */
    public static class ProductionConfig {
        public static final String ACCOUNT = "xy12345.us-east-1.aws";
        public static final String URL = "jdbc:snowflake://" + ACCOUNT + ".snowflakecomputing.com/";
        public static final String USER = "prod_java_service";
        public static final String PASSWORD = "Pr0d_J@v@_S3rv1c3_P@ss_2026!";
        public static final String WAREHOUSE = "PROD_ETL_WH";
        public static final String DATABASE = "PRODUCTION";
        public static final String SCHEMA = "ETL";
        public static final String ROLE = "ETL_ROLE";

        public static Connection getConnection() throws SQLException {
            Properties props = new Properties();
            props.put("user", USER);
            props.put("password", PASSWORD);
            props.put("warehouse", WAREHOUSE);
            props.put("db", DATABASE);
            props.put("schema", SCHEMA);
            props.put("role", ROLE);
            props.put("CLIENT_SESSION_KEEP_ALIVE", "true");

            return DriverManager.getConnection(URL, props);
        }
    }

    /**
     * Alternative URL formats
     */
    private static final String FULL_URL =
        "jdbc:snowflake://ab12345.us-west-2.snowflakecomputing.com/?" +
        "user=full_url_user&" +
        "password=Full_URL_P@ss_2026!&" +
        "db=FULL_URL_DB&" +
        "warehouse=FULL_URL_WH&" +
        "schema=PUBLIC&" +
        "role=FULL_URL_ROLE&" +
        "CLIENT_SESSION_KEEP_ALIVE=true&" +
        "tracing=ALL";
}
