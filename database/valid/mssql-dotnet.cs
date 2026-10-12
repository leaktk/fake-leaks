// Metadata: label=MS SQL Server connection strings in C#, type=database_connection, db_type=mssql, context=C# code, generator=manual

using System.Data.SqlClient;
using Microsoft.Extensions.Configuration;

namespace MyApp.Data
{
    public class DatabaseConfiguration
    {
        // Standard SQL Server connection string
        private const string ProductionConnectionString =
            "Server=mssql-prod.example.com,1433;Database=ProductionDB;User Id=sqluser;Password=MsSql_P@ssw0rd_2024!;Encrypt=True;TrustServerCertificate=False;";

        // Windows Authentication (with explicit credentials)
        private const string WindowsAuthConnection =
            "Server=sql-server.internal.example.com;Database=InternalDB;User Id=DOMAIN\\sqlservice;Password=D0m@in_P@ss_2024;Integrated Security=False;";

        // Azure SQL Database
        private const string AzureSqlConnection =
            "Server=tcp:myserver.database.windows.net,1433;Initial Catalog=AzureDB;Persist Security Info=False;User ID=azureuser;Password=@zur3_Sql_P@ss_2024!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";

        // Connection string with additional options
        private const string AnalyticsConnection =
            "Data Source=analytics-sql.example.com,1433;Initial Catalog=AnalyticsDB;User ID=analytics_user;Password=An@lyt1cs_DB_P@ss!;MultipleActiveResultSets=True;Application Name=AnalyticsApp;";

        // From configuration
        public static SqlConnection GetConnection(IConfiguration config)
        {
            var connectionString = config.GetConnectionString("DefaultConnection")
                ?? "Server=localhost,1433;Database=LocalDB;User Id=sa;Password=L0c@l_SA_P@ss_2024!;";

            return new SqlConnection(connectionString);
        }

        // Named instance connection
        private const string NamedInstanceConnection =
            "Server=SQLSERVER\\INSTANCE1;Database=MyDatabase;User Id=dbuser;Password=Inst@nc3_P@ss_2024;";
    }
}
