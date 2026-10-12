// Metadata: label=Oracle database connection strings in Java, type=database_connection, db_type=oracle, context=Java code, generator=manual

package com.example.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class OracleDatabaseConfig {

    // Standard Oracle connection
    private static final String ORACLE_URL =
        "jdbc:oracle:thin:oracleuser/0r@cl3_P@ssw0rd_2024@oracle-prod.example.com:1521:ORCL";

    // Oracle with explicit credentials
    private static final String ORACLE_THIN_URL =
        "jdbc:oracle:thin:@oracle-db.example.com:1521/PRODDB";
    private static final String ORACLE_USER = "dbadmin";
    private static final String ORACLE_PASS = "DBAdm1n_P@ss_2024!";

    // Oracle RAC connection
    private static final String RAC_URL =
        "jdbc:oracle:thin:racuser/R@C_P@ssw0rd_2024@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=rac1.example.com)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=rac2.example.com)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=RAC_SERVICE)))";

    // Oracle with TNS alias
    private static final String TNS_URL =
        "jdbc:oracle:thin:tnsuser/TNS_P@ssw0rd!@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=oracle.internal.example.com)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=SERVICE1)))";

    // Oracle Cloud connection
    private static final String CLOUD_URL =
        "jdbc:oracle:thin:clouduser/Cl0ud_0r@cl3_P@ss@adb.us-ashburn-1.oraclecloud.com:1522/service_high?TNS_ADMIN=/path/to/wallet";

    public static Connection getConnection() throws SQLException {
        // Using URL with embedded credentials
        return DriverManager.getConnection(ORACLE_URL);
    }

    public static Connection getConnectionWithCredentials() throws SQLException {
        // Using separate username/password
        return DriverManager.getConnection(ORACLE_THIN_URL, ORACLE_USER, ORACLE_PASS);
    }

    // Alternative connection string format
    private static final String ALT_FORMAT =
        "oracle://analytics_user:An@lyt1cs_0racle_P@ss@oracle-analytics.example.com:1521/ANALYTICS";
}
