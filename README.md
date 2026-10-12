# Fake Leaks

Synthetic secret data for testing and improving secret detection tools, leak scanners, and security tooling.

## Purpose

This repository contains **fake secrets** designed to test various git repository scanner configurations. **Nothing in this repo is a real secret.** All data is synthetic and generated specifically for testing purposes.

Use this repository to:
- Train machine learning models for secret detection
- Test and improve leak detection tools (GitLeaks, TruffleHog, etc.)
- Benchmark secret scanning accuracy (true positives vs false positives)
- Develop and validate new secret detection patterns
- Create test suites for security tooling

## ⚠️ Important

**All secrets in this repository are FAKE and should NEVER be used in production systems.**

## Repository Structure

Secrets are organized by type in dedicated directories, each containing `valid/` and `invalid/` subdirectories:

- **valid/**: Realistic secret examples that should be detected by scanners
- **invalid/**: False positives, placeholders, and edge cases that should NOT be flagged

## Secret Categories

### Authentication & Authorization
- **`jwt/`** - JWT tokens with various algorithms (HS256, RS256, ES256, etc.)
- **`auth-tokens/`** - OAuth2 tokens, bearer tokens, SAML assertions
- **`2fa/`** - TOTP secrets, backup codes, recovery keys
- **`basic-auth/`** - HTTP basic authentication credentials
- **`oidc/`** - OpenID Connect tokens and credentials

### Cloud Providers
- **`aws/`** - AWS access keys, secret keys, session tokens
- **`azure/`** - Azure subscription keys, storage account keys
- **`gcp/`** - Google Cloud Platform service account keys
- **`auth0/`** - Auth0 client secrets and management tokens

### Version Control & CI/CD
- **`github/`** - Personal access tokens, fine-grained tokens, OAuth tokens
- **`gitlab/`** - Personal access tokens, runner tokens, deploy tokens
- **`cicd/`** - CircleCI, Jenkins, Travis CI, Buildkite, GitHub Actions tokens

### API Keys & Services
- **`anthropic/`** - Claude API keys
- **`openai-api-keys`** - OpenAI API keys (project, service account, legacy)
- **`stripe/`** - Stripe secret, publishable, and restricted keys
- **`slack/`** - Slack bot tokens, user tokens, webhooks
- **`discord/`** - Discord bot tokens and webhook URLs
- **`telegram/`** - Telegram bot tokens
- **`twilio/`** - Twilio Account SID and Auth Token
- **`sendgrid/`** - SendGrid API keys
- **`mailchimp/`** - Mailchimp API keys
- **`datadog/`** - DataDog API and application keys
- **`pagerduty/`** - PagerDuty API tokens and integration keys
- **`sentry/`** - Sentry DSN and auth tokens
- **`launchdarkly/`** - LaunchDarkly SDK and API keys
- **`supabase/`** - Supabase anonymous and service role keys
- **`zoom/`** - Zoom JWT and OAuth credentials
- **`teams/`** - Microsoft Teams webhook URLs
- **`notion/`** - Notion integration tokens
- **`dropbox/`** - Dropbox API tokens
- **`huggingface/`** - HuggingFace API tokens
- **`sonarqube/`** - SonarQube tokens
- **`sourcegraph/`** - Sourcegraph access tokens
- **`sumologic/`** - Sumo Logic access IDs/keys, collector tokens, HTTP source URLs
- **`splunk/`** - Splunk authentication tokens, HEC tokens, API credentials
- **`label-studio/`** - Label Studio API tokens
- **`nvapi/`** - NVIDIA API keys
- **`groq/`** - Groq API keys
- **`picatic/`** - Picatic API tokens
- **`heroku/`** - Heroku API keys
- **`shopify/`** - Shopify API credentials
- **`snowflake/`** - Snowflake JWT tokens (legacy location, see `database/` for connection strings)

### Databases
- **`database/`** - Connection strings for PostgreSQL, MySQL, MongoDB, Redis, MSSQL, Oracle, Snowflake

### Cryptographic Keys
- **`pki/`** - RSA, ECDSA, Ed25519 private keys, SSH keys, certificates
- **`crypto/`** - AES keys, HMAC secrets, Age keys, GPG keys, ChaCha20 keys

### Infrastructure & Cloud Tools
- **`k8s/`** - Kubernetes service account tokens, kubeconfig files
- **`docker/`** - Docker registry credentials
- **`terraform/`** - Terraform Cloud tokens
- **`vault/`** - HashiCorp Vault tokens
- **`ansible/`** - Ansible Vault passwords
- **`hashicorp-vault/`** - Vault-specific configurations

### Password Hashes
- **`password-hash/`** - Bcrypt, Argon2, Scrypt, PBKDF2, MD5, SHA hashes
- **`htpasswd/`** - Apache htpasswd files

### Containers & Package Managers
- **`containers/`** - Container registry credentials
- **`npm/`** - NPM tokens
- **`maven/`** - Maven repository credentials
- **`gradle/`** - Gradle credentials

### Other
- **`generic/`** - Generic API keys and secrets
- **`settings/`** - Configuration files with embedded secrets
- **`secret-files/`** - Various secret file formats
- **`examples/`** - Example secret patterns
- **`semgrep-rules-examples/`** - Semgrep detection examples
- **`test/`** - Test fixtures and data

## Metadata Format

Each secret file includes metadata for documentation and tracking:

```
# Metadata:
# label: Human-readable description
# type: Secret type/category
# provider: Service/platform name
# context: Where this secret would appear (env var, config file, etc.)
# generator: How it was created (manual, secret_generator.py, etc.)
# valid: true/false (for invalid/ directory entries)
```

## Secret Generator

The `generators/secret_generator.py` script can programmatically generate synthetic secrets:

```bash
# Generate a JWT token
python generators/secret_generator.py --type jwt --algorithm HS256

# Generate an Anthropic API key
python generators/secret_generator.py --type api-key --provider anthropic

# Generate a PostgreSQL connection string
python generators/secret_generator.py --type db-connection --provider postgresql

# Get JSON output with metadata
python generators/secret_generator.py --type jwt --output json
```

See `generators/README.md` for complete documentation.

## Supported Secret Types

### JWT Tokens
- Algorithms: HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512, PS256
- Contexts: Environment variables, config files, HTTP headers, code
- Variations: Expired tokens, unsigned tokens, malformed tokens

### SSH & Cryptographic Keys
- **SSH**: Ed25519, RSA (2048/4096), ECDSA (P-256, P-384, P-521)
- **Formats**: OpenSSH, PEM, PKCS#8, authorized_keys, ssh_config
- **Certificates**: Certificate chains, client certs, CA certs

### API Keys
- 30+ providers with realistic token patterns
- Various formats: prefixed tokens, JWT-style, hex, base64
- Service-specific patterns (e.g., Stripe `sk_live_`, GitHub `ghp_`)

### Database Connection Strings
- PostgreSQL, MySQL, MongoDB, Redis, MSSQL, Oracle, Snowflake
- Formats: Standard URIs, connection strings, DSN, JDBC
- Contexts: Environment files, code, Docker Compose, YAML configs
- Snowflake-specific: Key-pair auth, OAuth, various account formats (AWS/Azure/GCP)

### Password Hashes
- **Algorithms**: Bcrypt, Argon2id, Scrypt, PBKDF2-SHA256/SHA512
- **Legacy**: MD5, SHA-256, SHA-512
- **Contexts**: Shadow files, database dumps, application configs

### 2FA & TOTP
- `otpauth://` URIs for various services
- Backup codes and recovery keys
- Base32-encoded TOTP secrets

### Cloud & Infrastructure
- Terraform Cloud tokens
- Kubernetes service account tokens
- HashiCorp Vault tokens
- Ansible Vault encrypted data
- Docker registry credentials

## Testing Your Scanner

### Basic Test
```bash
# Clone the repository
git clone https://github.com/your-org/fake-leaks.git

# Run your scanner
gitleaks detect --source ./fake-leaks
trufflehog filesystem ./fake-leaks
```

### Measuring Accuracy

**True Positives**: Secrets in `*/valid/` directories should be detected

**False Positives**: Items in `*/invalid/` directories should NOT be detected

Calculate metrics:
- **Precision** = True Positives / (True Positives + False Positives)
- **Recall** = True Positives / (True Positives + False Negatives)
- **F1 Score** = 2 × (Precision × Recall) / (Precision + Recall)

### Custom Rules

Use this repository to test custom detection rules:

```toml
# Example .gitleaks.toml rule
[[rules]]
    id = "anthropic-api-key"
    description = "Anthropic API Key"
    regex = '''sk-ant-api03-[A-Za-z0-9_-]{95}AA'''
    tags = ["api", "anthropic"]
```

## Contributing

When adding new synthetic secrets:

1. **Create valid examples** in `<type>/valid/`
2. **Create invalid examples** in `<type>/invalid/` (placeholders, false positives)
3. **Include metadata** in comments at the top of each file
4. **Use realistic patterns** based on actual service documentation
5. **Never commit real secrets** - all data must be synthetic

### Generating New Secrets

Use the generator script for consistency:

```bash
python generators/secret_generator.py --type api-key --provider newservice
```

Or create manually following the metadata format.

## Security Notice

This repository is designed to trigger secret detection tools. It is not suitable for:
- Production use
- Storing real credentials
- Security training with real systems
- Penetration testing without explicit authorization

## License

See [LICENSE](LICENSE) file.

## Changelog

### 2026 Update
- Added 200+ new synthetic secrets across 30+ categories
- Created `secret_generator.py` for programmatic secret generation
- Added JWT tokens with 9 different algorithms
- Expanded SSH keys: Ed25519, ECDSA (P-256, P-384, P-521)
- Added database connection strings (PostgreSQL, MySQL, MongoDB, Redis, MSSQL, Oracle, Snowflake)
- Added 25+ new API provider examples (Anthropic, Supabase, Discord, Telegram, Sumo Logic, Splunk, etc.)
- Added comprehensive password hashes (Bcrypt, Argon2, Scrypt, PBKDF2)
- Added 2FA/TOTP secrets and backup codes
- Added encryption keys (AES, ChaCha20, Age, GPG)
- Added OAuth2 tokens, Bearer tokens, SAML assertions
- Added cloud infrastructure tokens (Terraform, Vault, K8s, Ansible)
- Added CI/CD platform tokens (CircleCI, Jenkins, GitHub Actions, GitLab CI, etc.)
- Added certificate chains and client certificates
- Improved metadata documentation format
- Organized all secrets into valid/invalid subdirectories

## References

- [GitLeaks](https://github.com/gitleaks/gitleaks)
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [detect-secrets](https://github.com/Yelp/detect-secrets)
- [GitHub Token Formats](https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/)
