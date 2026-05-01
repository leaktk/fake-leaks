# Synthetic Data Generator (SDG) Improvements

This document outlines the improvements made to `generators/secret_generator.py` based on code review feedback.

## Summary of Changes

### 1. AWS Credentials Format Fixes
**Issue**: AWS access keys were using incorrect character set, secret keys had wrong format.

**Changes**:
- **Access Keys**: Now use base32 format `AKIA[A-Z2-7]{16}` instead of alphanumeric
  - Before: `AKIA` + 16 random uppercase letters/digits
  - After: `AKIA` + 16 random base32 characters (A-Z, 2-7)
  - Example: `AKIA74EEKAQTGEBOKYRT`

- **Secret Keys**: Now follow pattern `[A-Za-z0-9/\+=]{40}`
  - Before: 30-char base64 string
  - After: Exactly 40 characters from valid charset
  - Example: `+tNCxb+2/lwdIsrg1mn7MT5Z5AqMgwrF20HS9uhi`

**Reference**: https://aws.amazon.com/blogs/security/a-safer-way-to-distribute-aws-credentials-to-ec2/

---

### 2. GitHub Token Checksums
**Issue**: GitHub tokens didn't include proper CRC32 checksums.

**Changes**:
- Implemented CRC32 checksum encoded in Base62
- Last 6 characters of each token are now the checksum
- Added `_generate_github_token()` helper method
- Applies to: `ghp_` (PAT), `gho_` (OAuth), and fine-grained tokens

**Example**: `ghp_NIJhqEuWZZ3eFSEMD3IvGFxDaGqDMu3a0Gn1`
- Body: `NIJhqEuWZZ3eFSEMD3IvGFxDaGqDMu` (30 chars)
- Checksum: `3a0Gn1` (6 chars, Base62-encoded CRC32)

**Reference**: https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/

---

### 3. GitLab Token Structure
**Issue**: GitLab tokens were simple random strings, didn't match newer structured format.

**Changes**:
- Implemented full GitLab Routable Personal Access Token format
- Includes organization ID and user ID routing information
- Proper CRC32 checksum (Base36, 7 chars)
- Added `_generate_gitlab_token()` helper method

**Format**: `glpat-<base64_payload>.<version>.<length><crc32>`

**Example**: `glpat-Ba3rJQ49fe3EIbJGyP_8Rm86ZXZnegp1OjFmdW8N.01.140hkifhw`

**Reference**: https://github.com/leaktk/hack/blob/main/sdg/gen-synth-gitlab-personal-access-token

---

### 4. Kubernetes Service Account Tokens
**Issue**: Used hardcoded JWT header instead of proper JWT generation.

**Changes**:
- Now uses `generate_jwt()` method with custom K8s claims
- Includes realistic namespace and service account names
- Generates proper RS256 JWT tokens
- Added `_generate_k8s_service_account_token()` helper method

**Claims included**:
- `kubernetes.io/serviceaccount/namespace`
- `kubernetes.io/serviceaccount/service-account.name`
- `kubernetes.io/serviceaccount/service-account.uid`

**Reference**: https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/

---

### 5. HashiCorp Vault Token Improvements
**Issue**: Fixed length, provider named incorrectly.

**Changes**:
- Renamed from `vault` to `hashicorp_vault`
- Now uses randomly varying length (20-40 characters)
- Format: `hvs.<random_base64>`

**Example**: `hvs.zkr7ezAv4OZ9Vl-zcLeM5SGGYbR3crUsMJHHtyDVP-l1pMqnVd10`

**Reference**: https://developer.hashicorp.com/vault/docs/concepts/tokens

---

### 6. Removed Ansible Vault Password
**Issue**: Too generic - vault passwords can be any password format.

**Changes**:
- Removed `ansible.vault_password` pattern entirely
- Ansible vault passwords are not specific enough to include in SDG

---

### 7. Format Reference URLs
**Issue**: No documentation references for secret formats.

**Changes**:
- Added comment with format reference URL above each provider pattern
- Helps maintainers verify and update formats
- Makes it easy to check if formats have changed

**Example**:
```python
# Format Reference: https://docs.stripe.com/keys
"stripe": {
    "secret": lambda: f"sk_live_{self.random_alphanum(24)}",
    ...
}
```

---

### 8. Removed Fake-Looking Words
**Issue**: Generated credentials contained obvious test values like "Test User", "password", "example".

**Changes**:

#### JWT Tokens
- Before: `"name": "Test User"`
- After: Randomly selected realistic names
  - Example: "Alex Smith", "Riley Chen", "Jordan Garcia"

#### Database Connection Strings
- Before: `username = "user"`, `host = "db-xxx.example.com"`
- After: `username = "dbadmin_xxx"`, `host = "db-xxx.prod-cluster.internal"`

#### Password Hashes
- Before: Default plaintext `"P@ssw0rd123!"`
- After: Generated realistic passwords
  - Example: "Phoenix268!w8wv", "Nexus241!lNyE"

#### TOTP Secrets
- Before: `issuer = "Example"`, `username = "user@example.com"`
- After: Realistic values
  - Issuers: "SecureAuth", "CloudSync", "DataVault", "NetOps"
  - Usernames: Random `@company.com`, `@corp.io`, `@platform.cloud`, etc.
  - Example: `9oi9w3z7@platform.cloud`

---

## New Helper Methods

### Checksum and Encoding
```python
random_base32(length)           # Generate A-Z2-7 charset
to_base36(num, min_length)      # Convert int to base36
to_base62(num, min_length)      # Convert int to base62
crc32_checksum(data, ...)       # Calculate CRC32 checksum
```

### Token Generation
```python
_generate_github_token(prefix, total_length)
_generate_github_token_checksum(total_length)
_generate_gitlab_token(org_id, user_id)
_generate_k8s_service_account_token()
```

---

## Testing

All changes have been tested and verified:

```bash
# Test AWS credentials
python generators/secret_generator.py --type api-key --provider aws --subtype access_key
python generators/secret_generator.py --type api-key --provider aws --subtype secret_key

# Test GitHub token with checksum
python generators/secret_generator.py --type api-key --provider github --subtype pat

# Test GitLab structured token
python generators/secret_generator.py --type api-key --provider gitlab --subtype personal

# Test K8s service account JWT
python generators/secret_generator.py --type cloud --provider k8s --subtype service_account

# Test HashiCorp Vault varying length
python generators/secret_generator.py --type cloud --provider hashicorp_vault

# Test realistic JWT names
python generators/secret_generator.py --type jwt --output json

# Test realistic TOTP
python generators/secret_generator.py --type totp --output json

# Test realistic password hashes
python generators/secret_generator.py --type password-hash --output json
```

---

## Impact

These improvements ensure that:

1. **Checksums work**: Secret scanning tools that validate checksums will correctly identify these as valid-looking credentials
2. **Format accuracy**: Tokens match real-world formats used by actual services
3. **Reduced false positives**: Tokens look realistic enough to avoid being filtered out as "obviously fake"
4. **Better testing**: Secret detection tools can be tested against high-fidelity synthetic data
5. **Documentation**: Format references make it easy to verify and maintain patterns

---

## Examples

See demo output:

```bash
=== SDG Improvements Demo ===

1. AWS Credentials (Base32 Access Keys, Proper Secret Key Format)
   Access Key: AKIA74EEKAQTGEBOKYRT
   Secret Key: +tNCxb+2/lwdIsrg1mn7MT5Z5AqMgwrF20HS9uhi

2. GitHub Token with CRC32 Checksum (last 6 chars)
   PAT: ghp_NIJhqEuWZZ3eFSEMD3IvGFxDaGqDMu3a0Gn1

3. GitLab Token with Proper Structure and Checksum
   Personal: glpat-Ba3rJQ49fe3EIbJGyP_8Rm86ZXZnegp1OjFmdW8N.01.140hkifhw

4. HashiCorp Vault Token with Varying Length
   Token: hvs.zkr7ezAv4OZ9Vl-zcLeM5SGGYbR3crUsMJHHtyDVP-l1pMqnVd10

5. K8s Service Account Token (Proper JWT with custom claims)
   Length: 578 characters

6. Realistic JWT (No 'Test User')
   Name: Alex Smith

7. Realistic TOTP (No 'Example' or 'user@example.com')
   Issuer: SecureAuth
   Username: 9oi9w3z7@platform.cloud

8. Realistic Password Hash (No 'P@ssw0rd123!')
   Plaintext: Phoenix268!w8wv
```
