// Metadata: label=Snowflake connection in Node.js, type=database_connection, db_type=snowflake, context=JavaScript code, generator=manual

const snowflake = require('snowflake-sdk');

// Basic connection configuration
const connectionOptions = {
  account: 'xy12345.us-east-1',
  username: 'nodejs_user',
  password: 'N0d3JS_Sn0wfl@ke_P@ss_2026!',
  warehouse: 'NODEJS_WH',
  database: 'NODEJS_DB',
  schema: 'PUBLIC',
  role: 'NODEJS_ROLE'
};

// Create connection
const connection = snowflake.createConnection(connectionOptions);

connection.connect((err, conn) => {
  if (err) {
    console.error('Unable to connect:', err.message);
  } else {
    console.log('Successfully connected to Snowflake');
  }
});

// Production configuration
const prodConfig = {
  account: 'xy12345.us-east-1.aws',
  username: 'prod_nodejs_service',
  password: 'Pr0d_N0d3_S3rv1c3_P@ss!',
  warehouse: 'PROD_API_WH',
  database: 'PRODUCTION',
  schema: 'API',
  role: 'API_SERVICE_ROLE',
  clientSessionKeepAlive: true,
  clientSessionKeepAliveHeartbeatFrequency: 3600
};

// OAuth configuration
const oauthConfig = {
  account: 'xy12345.us-east-1',
  username: 'oauth_nodejs_user@example.com',
  authenticator: 'OAUTH',
  token: '7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d',
  warehouse: 'OAUTH_NODEJS_WH',
  database: 'OAUTH_DB'
};

// Key-pair authentication
const fs = require('fs');
const crypto = require('crypto');

const privateKeyObject = crypto.createPrivateKey({
  key: fs.readFileSync('/app/secrets/snowflake_key.pem'),
  format: 'pem',
  passphrase: 'K3y_N0d3_P@ssPhr@s3_2026!'
});

const keyPairConfig = {
  account: 'xy12345.us-east-1',
  username: 'keypair_nodejs_user',
  privateKey: privateKeyObject.export({
    format: 'pem',
    type: 'pkcs8'
  }),
  warehouse: 'KEYPAIR_NODEJS_WH',
  database: 'SECURE_DB',
  schema: 'PROTECTED',
  role: 'KEYPAIR_NODEJS_ROLE'
};

// Environment-based configuration
const envConfig = {
  account: process.env.SNOWFLAKE_ACCOUNT || 'xy12345.us-east-1',
  username: process.env.SNOWFLAKE_USER || 'env_nodejs_user',
  password: process.env.SNOWFLAKE_PASSWORD || 'Env_N0d3_P@ss_2026!',
  warehouse: process.env.SNOWFLAKE_WAREHOUSE || 'ENV_WH',
  database: process.env.SNOWFLAKE_DATABASE || 'ENV_DB',
  schema: process.env.SNOWFLAKE_SCHEMA || 'PUBLIC',
  role: process.env.SNOWFLAKE_ROLE || 'ENV_ROLE'
};

// Multiple environment configurations
const configs = {
  development: {
    account: 'cd67890.us-west-2.aws',
    username: 'dev_user',
    password: 'D3v_Sn0wfl@ke_P@ss!',
    warehouse: 'DEV_WH',
    database: 'DEV_DB'
  },

  staging: {
    account: 'ef24680.us-central1.gcp',
    username: 'staging_user',
    password: 'St@g1ng_Sn0wfl@ke_P@ss!',
    warehouse: 'STAGING_WH',
    database: 'STAGING_DB'
  },

  production: {
    account: 'xy12345.us-east-1.aws',
    username: 'prod_user',
    password: 'Pr0d_Sn0wfl@ke_S3cr3t_2026!',
    warehouse: 'PROD_WH',
    database: 'PRODUCTION'
  }
};

module.exports = {
  connectionOptions,
  prodConfig,
  oauthConfig,
  keyPairConfig,
  envConfig,
  configs
};
