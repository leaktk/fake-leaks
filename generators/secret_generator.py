#!/usr/bin/env python3
"""
Synthetic Secret Generator for fake-leaks

This script generates synthetic secrets for testing secret detection tools.
All generated secrets are fake and should never be used in production.

Usage:
    python secret_generator.py --type jwt --algorithm HS256
    python secret_generator.py --type api-key --provider stripe
    python secret_generator.py --type ssh-key --key-type ed25519
"""

import argparse
import base64
import hashlib
import hmac
import json
import os
import random
import secrets
import string
import struct
import uuid
import zlib
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, Optional, List


class SecretGenerator:
    """Generate various types of synthetic secrets with metadata"""

    def __init__(self, seed: Optional[int] = None):
        """Initialize generator with optional seed for reproducibility"""
        if seed:
            random.seed(seed)

    # === Utility Functions ===

    @staticmethod
    def random_hex(length: int) -> str:
        """Generate random hex string"""
        return secrets.token_hex(length)

    @staticmethod
    def random_bytes(length: int) -> bytes:
        """Generate random bytes"""
        return secrets.token_bytes(length)

    @staticmethod
    def random_base64(length: int, url_safe: bool = False) -> str:
        """Generate random base64 string"""
        data = secrets.token_bytes(length)
        if url_safe:
            return base64.urlsafe_b64encode(data).decode().rstrip('=')
        return base64.b64encode(data).decode()

    @staticmethod
    def random_string(length: int, charset: str = string.ascii_letters + string.digits) -> str:
        """Generate random string from charset"""
        return ''.join(secrets.choice(charset) for _ in range(length))

    @staticmethod
    def random_alphanum(length: int) -> str:
        """Generate random alphanumeric string"""
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))

    @staticmethod
    def random_base32(length: int) -> str:
        """Generate random base32 string (A-Z2-7)"""
        charset = string.ascii_uppercase + '234567'
        return ''.join(secrets.choice(charset) for _ in range(length))

    @staticmethod
    def to_base36(num: int, min_length: int = 1) -> str:
        """Convert integer to base36 string"""
        if num == 0:
            return '0' * min_length
        charset = string.digits + string.ascii_lowercase
        result = []
        while num:
            num, rem = divmod(num, 36)
            result.append(charset[rem])
        return ''.join(reversed(result)).zfill(min_length)

    @staticmethod
    def to_base62(num: int, min_length: int = 6) -> str:
        """Convert integer to base62 string (for checksums)"""
        if num == 0:
            return '0' * min_length
        charset = string.digits + string.ascii_uppercase + string.ascii_lowercase
        result = []
        while num:
            num, rem = divmod(num, 62)
            result.append(charset[rem])
        return ''.join(reversed(result)).zfill(min_length)

    @staticmethod
    def crc32_checksum(data: str, base62_encode: bool = True, length: int = 6) -> str:
        """Calculate CRC32 checksum of string"""
        crc_val = zlib.crc32(data.encode('utf-8'))
        if base62_encode:
            return SecretGenerator.to_base62(crc_val, min_length=length)
        return SecretGenerator.to_base36(crc_val, min_length=length)

    # === Helper methods for specific token types ===

    def _generate_github_token(self, prefix: str, total_length: int) -> str:
        """Generate GitHub token with CRC32 checksum"""
        # GitHub tokens: last 6 chars are base62-encoded CRC32 checksum
        body_length = total_length - 6
        body = self.random_alphanum(body_length)
        token_prefix = f"{prefix}{body}"
        checksum = self.crc32_checksum(token_prefix, base62_encode=True, length=6)
        return f"{token_prefix}{checksum}"

    def _generate_github_token_checksum(self, total_length: int) -> str:
        """Generate GitHub token body with checksum (no prefix)"""
        body_length = total_length - 6
        body = self.random_alphanum(body_length)
        checksum = self.crc32_checksum(body, base62_encode=True, length=6)
        return f"{body}{checksum}"

    def _generate_gitlab_token(self, org_id: int = None, user_id: int = None) -> str:
        """
        Generate GitLab Routable Personal Access Token with proper structure and checksum
        Format Reference: https://github.com/leaktk/hack/blob/main/sdg/gen-synth-gitlab-personal-access-token
        """
        PREFIX = "glpat-"
        VERSION = 1
        VERSION_STR = self.to_base36(VERSION, min_length=2)

        # Use random IDs if not provided
        if org_id is None:
            org_id = random.randint(1, 999999)
        if user_id is None:
            user_id = random.randint(1, 999999)

        # Convert IDs to base36
        oid_b36 = self.to_base36(org_id)
        uid_b36 = self.to_base36(user_id)

        # Create routing payload
        routing_payload = f"o:{oid_b36}\nu:{uid_b36}"

        # Build encodable data: [16 random bytes] + [payload] + [size byte]
        random_bytes = secrets.token_bytes(16)
        payload_bytes = routing_payload.encode("utf-8")
        size_byte = struct.pack("B", len(payload_bytes))
        encodable_data = random_bytes + payload_bytes + size_byte

        # Base64 encode (URL-safe, no padding)
        b64_payload = base64.urlsafe_b64encode(encodable_data).decode("utf-8").rstrip("=")

        # Calculate length holder in base36
        length_holder = self.to_base36(len(b64_payload), min_length=2)

        # Assemble token before CRC
        pre_crc_token = f"{PREFIX}{b64_payload}.{VERSION_STR}.{length_holder}"

        # Calculate CRC32 checksum (base36, 7 chars)
        crc_str = self.crc32_checksum(pre_crc_token, base62_encode=False, length=7)

        return f"{pre_crc_token}{crc_str}"

    def _generate_k8s_service_account_token(self) -> str:
        """Generate Kubernetes service account token using proper JWT"""
        # K8s service account tokens are JWTs with specific claims
        namespaces = ["kube-system", "default", "production", "staging", "monitoring"]
        service_accounts = ["default", "admin", "deployer", "metrics-server", "ingress-controller"]

        custom_claims = {
            "kubernetes.io/serviceaccount/namespace": random.choice(namespaces),
            "kubernetes.io/serviceaccount/service-account.name": random.choice(service_accounts),
            "kubernetes.io/serviceaccount/service-account.uid": str(uuid.uuid4())
        }

        result = self.generate_jwt(algorithm="RS256", custom_claims=custom_claims)
        return result["token"]

    # === JWT Tokens ===

    def generate_jwt(self, algorithm: str = "HS256", include_signature: bool = True,
                     expired: bool = False, custom_claims: Optional[Dict] = None) -> Dict[str, Any]:
        """Generate synthetic JWT token"""

        # Header
        header = {
            "alg": algorithm,
            "typ": "JWT"
        }

        # Claims
        now = datetime.now(timezone.utc)
        exp_time = now - timedelta(days=30) if expired else now + timedelta(days=365)

        # Generate realistic-looking name
        first_names = ["Jordan", "Morgan", "Casey", "Riley", "Alex", "Quinn", "Taylor", "Avery"]
        last_names = ["Chen", "Smith", "Johnson", "Williams", "Brown", "Garcia", "Martinez", "Lee"]
        name = f"{random.choice(first_names)} {random.choice(last_names)}"

        claims = {
            "sub": str(uuid.uuid4()),
            "name": name,
            "iat": int(now.timestamp()),
            "exp": int(exp_time.timestamp()),
            "jti": str(uuid.uuid4())
        }

        if custom_claims:
            claims.update(custom_claims)

        # Encode header and payload
        header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip('=')
        payload_b64 = base64.urlsafe_b64encode(json.dumps(claims).encode()).decode().rstrip('=')

        # Generate signature (fake but valid-looking)
        if include_signature:
            signature_data = self.random_base64(32, url_safe=True)
            token = f"{header_b64}.{payload_b64}.{signature_data}"
        else:
            token = f"{header_b64}.{payload_b64}"

        return {
            "token": token,
            "metadata": {
                "label": f"Synthetic JWT Token ({algorithm})",
                "type": "jwt",
                "algorithm": algorithm,
                "expired": expired,
                "has_signature": include_signature,
                "generator": "secret_generator.py::generate_jwt"
            }
        }

    # === API Keys ===

    def generate_api_key(self, provider: str, key_type: str = "secret") -> Dict[str, Any]:
        """Generate synthetic API key for various providers"""

        patterns = {
            # Format Reference: https://docs.anthropic.com/en/api/getting-started
            "anthropic": {
                "secret": lambda: f"sk-ant-api03-{self.random_base64(40, True)}-{self.random_base64(40, True)}AA",
                "label": "Anthropic API Key"
            },
            # Format Reference: https://platform.openai.com/docs/api-reference/authentication
            "openai": {
                "secret": lambda: f"sk-{self.random_alphanum(48)}",
                "project_user": lambda: f"sk-proj-{self.random_alphanum(20)}T3BlbkFJ{self.random_alphanum(20)}",
                "project_service": lambda: f"sk-svcacct-{self.random_alphanum(20)}T3BlbkFJ{self.random_alphanum(20)}",
                "label": "OpenAI API Key"
            },
            # Format Reference: https://docs.stripe.com/keys
            "stripe": {
                "secret": lambda: f"sk_live_{self.random_alphanum(24)}",
                "publishable": lambda: f"pk_live_{self.random_alphanum(24)}",
                "restricted": lambda: f"rk_live_{self.random_alphanum(24)}",
                "label": "Stripe API Key"
            },
            # Format Reference: https://github.blog/2021-04-05-behind-githubs-new-authentication-token-formats/
            "github": {
                "pat": lambda: self._generate_github_token("ghp_", 36),
                "fine_grained": lambda: f"github_pat_{self.random_alphanum(22)}_{self._generate_github_token_checksum(59)}",
                "oauth": lambda: self._generate_github_token("gho_", 36),
                "label": "GitHub Token"
            },
            # Format Reference: https://github.com/leaktk/hack/blob/main/sdg/gen-synth-gitlab-personal-access-token
            "gitlab": {
                "personal": lambda: self._generate_gitlab_token(),
                "oauth": lambda: f"gloa-{self.random_alphanum(64)}",
                "label": "GitLab Token"
            },
            # Format Reference: https://aws.amazon.com/blogs/security/a-safer-way-to-distribute-aws-credentials-to-ec2/
            "aws": {
                "access_key": lambda: f"AKIA{self.random_base32(16)}",
                "secret_key": lambda: self.random_string(40, string.ascii_letters + string.digits + '/+='),
                "label": "AWS Credentials"
            },
            # Format Reference: https://api.slack.com/authentication/token-types
            "slack": {
                "bot": lambda: f"xoxb-{self.random_string(12, string.digits)}-{self.random_string(12, string.digits)}-{self.random_alphanum(24)}",
                "user": lambda: f"xoxp-{self.random_string(12, string.digits)}-{self.random_string(12, string.digits)}-{self.random_alphanum(24)}",
                "webhook": lambda: f"https://hooks.slack.com/services/T{self.random_alphanum(8)}/B{self.random_alphanum(8)}/{self.random_alphanum(24)}",
                "label": "Slack Token"
            },
            # Format Reference: https://discord.com/developers/docs/reference#authentication
            "discord": {
                "bot": lambda: f"MTA{self.random_string(17, string.digits)}.{self.random_base64(6, True)}.{self.random_base64(27, True)}",
                "label": "Discord Bot Token"
            },
            # Format Reference: https://core.telegram.org/bots/api#authorizing-your-bot
            "telegram": {
                "bot": lambda: f"{self.random_string(10, string.digits)}:AAH{self.random_alphanum(32)}",
                "label": "Telegram Bot Token"
            },
            # Format Reference: https://www.twilio.com/docs/iam/credentials/api
            "twilio": {
                "account_sid": lambda: f"AC{self.random_hex(16)}",
                "auth_token": lambda: self.random_hex(16),
                "label": "Twilio Credentials"
            },
            # Format Reference: https://docs.datadoghq.com/account_management/api-app-keys/
            "datadog": {
                "api_key": lambda: self.random_hex(16),
                "app_key": lambda: self.random_hex(20),
                "label": "DataDog API Key"
            },
            # Format Reference: https://docs.sendgrid.com/ui/account-and-settings/api-keys
            "sendgrid": {
                "api_key": lambda: f"SG.{self.random_base64(22, True)}.{self.random_base64(43, True)}",
                "label": "SendGrid API Key"
            },
            # Format Reference: https://mailchimp.com/developer/marketing/guides/quick-start/
            "mailchimp": {
                "api_key": lambda: f"{self.random_hex(16)}-us{random.randint(1, 20)}",
                "label": "Mailchimp API Key"
            },
            # Format Reference: https://docs.sentry.io/api/auth/
            "sentry": {
                "dsn": lambda: f"https://{self.random_hex(16)}@o{random.randint(100000, 999999)}.ingest.sentry.io/{random.randint(1000000, 9999999)}",
                "auth_token": lambda: self.random_hex(32),
                "label": "Sentry DSN/Token"
            },
            # Format Reference: https://developer.pagerduty.com/docs/rest-api-v2/authentication/
            "pagerduty": {
                "api_key": lambda: f"u+{self.random_alphanum(18)}",
                "integration_key": lambda: self.random_hex(16),
                "label": "PagerDuty Token"
            },
            # Format Reference: https://docs.launchdarkly.com/sdk/concepts/client-side-server-side#keys
            "launchdarkly": {
                "sdk_key": lambda: f"sdk-{self.random_hex(16)}",
                "mobile_key": lambda: f"mob-{self.random_hex(16)}",
                "label": "LaunchDarkly Key"
            },
            # Format Reference: https://supabase.com/docs/guides/api/api-keys
            "supabase": {
                "anon_key": lambda: f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.{self.random_base64(100, True)}.{self.random_base64(43, True)}",
                "service_role": lambda: f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.{self.random_base64(120, True)}.{self.random_base64(43, True)}",
                "label": "Supabase Key"
            }
        }

        if provider not in patterns:
            raise ValueError(f"Unknown provider: {provider}")

        pattern_info = patterns[provider]

        # Get the appropriate key generator
        if key_type in pattern_info:
            key = pattern_info[key_type]()
        elif "secret" in pattern_info:
            key = pattern_info["secret"]()
        else:
            # Use the first non-label key
            for k, v in pattern_info.items():
                if k != "label" and callable(v):
                    key = v()
                    break

        return {
            "key": key,
            "metadata": {
                "label": f"{pattern_info['label']} ({key_type})",
                "type": "api_key",
                "provider": provider,
                "key_type": key_type,
                "generator": "secret_generator.py::generate_api_key"
            }
        }

    # === Database Connection Strings ===

    def generate_db_connection_string(self, db_type: str, include_credentials: bool = True) -> Dict[str, Any]:
        """Generate synthetic database connection string"""

        username = f"dbadmin_{self.random_alphanum(6)}" if include_credentials else "dbadmin"
        password = self.random_base64(16) if include_credentials else self.random_base64(12)
        host = f"db-{self.random_alphanum(8)}.prod-cluster.internal"
        port_map = {
            "postgresql": 5432,
            "mysql": 3306,
            "mongodb": 27017,
            "redis": 6379,
            "mssql": 1433,
            "oracle": 1521
        }

        patterns = {
            "postgresql": f"postgresql://{username}:{password}@{host}:{port_map['postgresql']}/mydb?sslmode=require",
            "mysql": f"mysql://{username}:{password}@{host}:{port_map['mysql']}/mydb",
            "mongodb": f"mongodb://{username}:{password}@{host}:{port_map['mongodb']}/mydb?authSource=admin",
            "mongodb_srv": f"mongodb+srv://{username}:{password}@{host}/mydb",
            "redis": f"redis://{username}:{password}@{host}:{port_map['redis']}/0",
            "mssql": f"Server={host},{port_map['mssql']};Database=mydb;User Id={username};Password={password};",
            "oracle": f"oracle://{username}:{password}@{host}:{port_map['oracle']}/ORCL"
        }

        if db_type not in patterns:
            raise ValueError(f"Unknown database type: {db_type}")

        return {
            "connection_string": patterns[db_type],
            "metadata": {
                "label": f"Synthetic {db_type.title()} Connection String",
                "type": "database_connection",
                "db_type": db_type,
                "has_credentials": include_credentials,
                "generator": "secret_generator.py::generate_db_connection_string"
            }
        }

    # === Password Hashes ===

    def generate_password_hash(self, hash_type: str, password: str = None) -> Dict[str, Any]:
        """Generate synthetic password hash"""

        # Generate realistic password if not provided
        if password is None:
            words = ["Quantum", "Neural", "Crypto", "Matrix", "Vector", "Phoenix", "Nexus", "Cipher"]
            password = f"{random.choice(words)}{random.randint(100, 999)}!{self.random_alphanum(4)}"

        hashes = {
            "md5": lambda p: hashlib.md5(p.encode()).hexdigest(),
            "sha256": lambda p: hashlib.sha256(p.encode()).hexdigest(),
            "sha512": lambda p: hashlib.sha512(p.encode()).hexdigest(),
            "bcrypt": lambda p: f"$2b$12${self.random_base64(22, False).replace('+', '.').replace('/', '.')[:22]}{self.random_base64(31, False).replace('+', '.').replace('/', '.')}",
            "argon2": lambda p: f"$argon2id$v=19$m=65536,t=3,p=4${self.random_base64(22, True)},{self.random_base64(43, True)}",
            "scrypt": lambda p: f"$scrypt$ln=16,r=8,p=1${self.random_base64(32, True)}${self.random_base64(64, True)}",
            "pbkdf2_sha256": lambda p: f"pbkdf2_sha256$260000${self.random_alphanum(22)}${self.random_base64(44, False)}"
        }

        if hash_type not in hashes:
            raise ValueError(f"Unknown hash type: {hash_type}")

        return {
            "hash": hashes[hash_type](password),
            "metadata": {
                "label": f"Synthetic {hash_type.upper()} Password Hash",
                "type": "password_hash",
                "hash_type": hash_type,
                "plaintext": password,
                "generator": "secret_generator.py::generate_password_hash"
            }
        }

    # === Encryption Keys ===

    def generate_encryption_key(self, key_type: str) -> Dict[str, Any]:
        """Generate synthetic encryption key"""

        patterns = {
            "aes_256": lambda: self.random_hex(32),  # 256 bits
            "aes_128": lambda: self.random_hex(16),  # 128 bits
            "chacha20": lambda: self.random_hex(32),  # 256 bits
            "hmac_secret": lambda: self.random_base64(32),
            "webhook_secret": lambda: self.random_alphanum(32),
            "age": lambda: f"AGE-SECRET-KEY-{self.random_string(58, string.ascii_uppercase + string.digits).upper()}"
        }

        if key_type not in patterns:
            raise ValueError(f"Unknown encryption key type: {key_type}")

        return {
            "key": patterns[key_type](),
            "metadata": {
                "label": f"Synthetic {key_type.upper()} Key",
                "type": "encryption_key",
                "key_type": key_type,
                "generator": "secret_generator.py::generate_encryption_key"
            }
        }

    # === OAuth & Auth Tokens ===

    def generate_oauth_token(self, token_type: str = "access") -> Dict[str, Any]:
        """Generate synthetic OAuth token"""

        patterns = {
            "access": lambda: self.random_base64(32, True),
            "refresh": lambda: self.random_base64(48, True),
            "bearer": lambda: f"Bearer {self.random_base64(32, True)}"
        }

        token = patterns.get(token_type, patterns["access"])()

        return {
            "token": token,
            "metadata": {
                "label": f"Synthetic OAuth {token_type.title()} Token",
                "type": "oauth_token",
                "token_type": token_type,
                "generator": "secret_generator.py::generate_oauth_token"
            }
        }

    # === CI/CD Tokens ===

    def generate_cicd_token(self, platform: str) -> Dict[str, Any]:
        """Generate synthetic CI/CD platform token"""

        patterns = {
            "circleci": lambda: self.random_hex(20),
            "travis": lambda: self.random_alphanum(22),
            "jenkins": lambda: self.random_hex(16),
            "buildkite": lambda: f"bkua_{self.random_alphanum(40)}",
            "drone": lambda: self.random_alphanum(32),
            "gitlab_runner": lambda: f"GR1348941{self.random_alphanum(20)}",
            "github_actions": lambda: f"ghs_{self.random_alphanum(36)}"
        }

        if platform not in patterns:
            raise ValueError(f"Unknown CI/CD platform: {platform}")

        return {
            "token": patterns[platform](),
            "metadata": {
                "label": f"Synthetic {platform.title()} Token",
                "type": "cicd_token",
                "platform": platform,
                "generator": "secret_generator.py::generate_cicd_token"
            }
        }

    # === 2FA & TOTP ===

    def generate_totp_secret(self, issuer: str = None, username: str = None) -> Dict[str, Any]:
        """Generate synthetic TOTP secret"""

        # Generate realistic issuer and username if not provided
        if issuer is None:
            issuers = ["Acme Corp", "CloudSync", "DataVault", "SecureAuth", "NetOps", "DevPortal"]
            issuer = random.choice(issuers)
        if username is None:
            domains = ["company.com", "corp.io", "enterprise.net", "tech.dev", "platform.cloud"]
            username = f"{self.random_alphanum(8).lower()}@{random.choice(domains)}"

        secret = self.random_base64(20, False).replace('+', '').replace('/', '').replace('=', '').upper()
        uri = f"otpauth://totp/{issuer}:{username}?secret={secret}&issuer={issuer}&algorithm=SHA1&digits=6&period=30"

        # Generate backup codes
        backup_codes = [f"{self.random_string(4, string.digits)}-{self.random_string(4, string.digits)}" for _ in range(10)]

        return {
            "uri": uri,
            "secret": secret,
            "backup_codes": backup_codes,
            "metadata": {
                "label": "Synthetic TOTP Secret",
                "type": "totp_secret",
                "issuer": issuer,
                "username": username,
                "generator": "secret_generator.py::generate_totp_secret"
            }
        }

    # === Cloud Platform Tokens ===

    def generate_cloud_token(self, provider: str, token_type: str = "default") -> Dict[str, Any]:
        """Generate synthetic cloud platform token"""

        patterns = {
            # Format Reference: https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/api-tokens
            "terraform": {
                "token": lambda: f"{self.random_alphanum(14)}.atlasv1.{self.random_base64(64, True)}"
            },
            # Format Reference: https://developer.hashicorp.com/vault/docs/concepts/tokens
            "hashicorp_vault": {
                "token": lambda: f"hvs.{self.random_base64(random.randint(20, 40), True)}"
            },
            # Format Reference: https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/
            "k8s": {
                "service_account": lambda: self._generate_k8s_service_account_token()
            }
        }

        if provider not in patterns:
            raise ValueError(f"Unknown cloud provider: {provider}")

        token_gen = patterns[provider].get(token_type) or list(patterns[provider].values())[0]

        return {
            "token": token_gen(),
            "metadata": {
                "label": f"Synthetic {provider.title()} Token",
                "type": "cloud_token",
                "provider": provider,
                "token_type": token_type,
                "generator": "secret_generator.py::generate_cloud_token"
            }
        }


def main():
    """CLI interface for secret generator"""
    parser = argparse.ArgumentParser(description="Generate synthetic secrets for testing")
    parser.add_argument("--type", required=True,
                       choices=["jwt", "api-key", "db-connection", "password-hash",
                               "encryption-key", "oauth", "cicd", "totp", "cloud"],
                       help="Type of secret to generate")
    parser.add_argument("--provider", help="Provider/platform name")
    parser.add_argument("--subtype", help="Subtype of secret")
    parser.add_argument("--algorithm", help="Algorithm (for JWT)")
    parser.add_argument("--seed", type=int, help="Random seed for reproducibility")
    parser.add_argument("--output", choices=["json", "text"], default="text", help="Output format")

    args = parser.parse_args()

    generator = SecretGenerator(seed=args.seed)
    result = None

    try:
        if args.type == "jwt":
            algorithm = args.algorithm or "HS256"
            result = generator.generate_jwt(algorithm=algorithm)

        elif args.type == "api-key":
            if not args.provider:
                print("Error: --provider required for api-key type")
                return 1
            result = generator.generate_api_key(args.provider, args.subtype or "secret")

        elif args.type == "db-connection":
            if not args.provider:
                print("Error: --provider required for db-connection type")
                return 1
            result = generator.generate_db_connection_string(args.provider)

        elif args.type == "password-hash":
            hash_type = args.subtype or "bcrypt"
            result = generator.generate_password_hash(hash_type)

        elif args.type == "encryption-key":
            key_type = args.subtype or "aes_256"
            result = generator.generate_encryption_key(key_type)

        elif args.type == "oauth":
            token_type = args.subtype or "access"
            result = generator.generate_oauth_token(token_type)

        elif args.type == "cicd":
            if not args.provider:
                print("Error: --provider required for cicd type")
                return 1
            result = generator.generate_cicd_token(args.provider)

        elif args.type == "totp":
            result = generator.generate_totp_secret()

        elif args.type == "cloud":
            if not args.provider:
                print("Error: --provider required for cloud type")
                return 1
            result = generator.generate_cloud_token(args.provider, args.subtype or "default")

        if result:
            if args.output == "json":
                print(json.dumps(result, indent=2))
            else:
                # Print the main value
                if "token" in result:
                    print(result["token"])
                elif "key" in result:
                    print(result["key"])
                elif "connection_string" in result:
                    print(result["connection_string"])
                elif "hash" in result:
                    print(result["hash"])
                elif "uri" in result:
                    print(result["uri"])

    except ValueError as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
