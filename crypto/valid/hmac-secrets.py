# Metadata: label=HMAC secrets, type=encryption_key, key_type=hmac, context=Python code, generator=secret_generator.py

import hmac
import hashlib
import base64

class HMACConfig:
    # HMAC secrets for signing
    HMAC_SECRET = b'5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a'
    JWT_SECRET = 'super-secret-jwt-signing-key-change-in-production'
    API_SIGNING_SECRET = 'api-request-signing-secret-key-2024'

    # Base64 encoded HMAC secrets
    HMAC_SECRET_B64 = 'OWUwZjFhMmIzYzRkNWU2ZjdhOGI5YzBkMWUyZjNhNGI='

def sign_message(message: str) -> str:
    """Sign a message with HMAC-SHA256"""
    signature = hmac.new(
        HMACConfig.HMAC_SECRET,
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    return signature

# Webhook signing secrets
WEBHOOK_SECRETS = {
    'github': 'whsec_7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e',
    'stripe': 'whsec_3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a',
    'slack': 'v1,1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e',
    'twilio': '9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a'
}

# Cookie signing secret
COOKIE_SECRET = 'cookie-session-signing-secret-key-random-2024'
SESSION_SECRET = 's3ss10n-s1gn1ng-s3cr3t-k3y-2024'
