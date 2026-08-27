# Metadata: label=Twilio credentials, type=api_key, provider=twilio, context=Python code, generator=secret_generator.py

from twilio.rest import Client

class TwilioConfig:
    # Account SID and Auth Token
    ACCOUNT_SID = "AC7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a"
    AUTH_TOKEN = "3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e"

    # Alternative credentials
    SUBACCOUNT_SID = "ACa1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6"
    SUBACCOUNT_TOKEN = "9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c"

    # API Key credentials (alternative auth method)
    API_KEY_SID = "SK4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9"
    API_KEY_SECRET = "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d"

def get_client():
    return Client(TwilioConfig.ACCOUNT_SID, TwilioConfig.AUTH_TOKEN)

# Environment variable format
import os
os.environ['TWILIO_ACCOUNT_SID'] = 'ACf6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c'
os.environ['TWILIO_AUTH_TOKEN'] = 'd7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2'
