# Secret Generators

This directory contains scripts for generating synthetic secrets for testing leak detection tools.

## secret_generator.py

A comprehensive Python script for generating various types of fake secrets with metadata.

### Usage Examples

```bash
# Generate a JWT token with HS256 algorithm
python generators/secret_generator.py --type jwt --algorithm HS256

# Generate an Anthropic API key
python generators/secret_generator.py --type api-key --provider anthropic

# Generate a Stripe secret key
python generators/secret_generator.py --type api-key --provider stripe --subtype secret

# Generate a PostgreSQL connection string
python generators/secret_generator.py --type db-connection --provider postgresql

# Generate a bcrypt password hash
python generators/secret_generator.py --type password-hash --subtype bcrypt

# Generate an AES-256 encryption key
python generators/secret_generator.py --type encryption-key --subtype aes_256

# Generate a TOTP secret with QR code URI
python generators/secret_generator.py --type totp

# Get JSON output with metadata
python generators/secret_generator.py --type jwt --algorithm RS256 --output json
```

### Supported Secret Types

- **jwt**: JWT tokens with various algorithms (HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512)
- **api-key**: API keys for multiple providers:
  - anthropic, openai, stripe, github, gitlab, aws, slack, discord, telegram
  - twilio, datadog, sendgrid, mailchimp, sentry, pagerduty, launchdarkly, supabase
- **db-connection**: Database connection strings:
  - postgresql, mysql, mongodb, mongodb_srv, redis, mssql, oracle
- **password-hash**: Password hashes:
  - md5, sha256, sha512, bcrypt, argon2, scrypt, pbkdf2_sha256
- **encryption-key**: Encryption keys:
  - aes_256, aes_128, chacha20, hmac_secret, webhook_secret, age
- **oauth**: OAuth tokens (access, refresh, bearer)
- **cicd**: CI/CD platform tokens:
  - circleci, travis, jenkins, buildkite, drone, gitlab_runner, github_actions
- **totp**: TOTP secrets with otpauth:// URIs and backup codes
- **cloud**: Cloud platform tokens:
  - terraform, vault, ansible, k8s

### Metadata Format

Each generated secret includes metadata for documentation:

```json
{
  "token": "eyJhbGc...",
  "metadata": {
    "label": "Synthetic JWT Token (HS256)",
    "type": "jwt",
    "algorithm": "HS256",
    "expired": false,
    "has_signature": true,
    "generator": "secret_generator.py::generate_jwt"
  }
}
```

### Reproducibility

Use the `--seed` flag to generate the same secrets consistently:

```bash
python generators/secret_generator.py --type jwt --seed 12345
```
