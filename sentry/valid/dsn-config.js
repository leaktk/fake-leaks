// Metadata: label=Sentry DSN and tokens, type=api_key, provider=sentry, context=JavaScript configuration, generator=secret_generator.py

import * as Sentry from "@sentry/react";

// Sentry DSN (Data Source Name)
const SENTRY_DSN = "https://5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d@o123456.ingest.sentry.io/7654321";

// Alternative DSNs for different environments
const SENTRY_CONFIG = {
  production: {
    dsn: "https://1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c@o987654.ingest.sentry.io/1234567",
    environment: "production"
  },
  staging: {
    dsn: "https://9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a@o456789.ingest.sentry.io/9876543",
    environment: "staging"
  }
};

// Sentry Auth Token (for API access)
const SENTRY_AUTH_TOKEN = "3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e";

// Initialize Sentry
Sentry.init({
  dsn: SENTRY_DSN,
  authToken: SENTRY_AUTH_TOKEN,
  tracesSampleRate: 1.0,
});

// Internal integration token
const INTERNAL_INTEGRATION_TOKEN = "sntrys_7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b";

export { SENTRY_DSN, SENTRY_AUTH_TOKEN };
