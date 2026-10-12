# Metadata: label=Sumo Logic API credentials in Python, type=api_key, provider=sumologic, context=Python code, generator=manual

import os
from sumologic import SumoLogic

class SumoLogicConfig:
    # API credentials
    ACCESS_ID = "suABCDEF123456789"
    ACCESS_KEY = "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"

    # API endpoint (varies by deployment)
    ENDPOINT = "https://api.sumologic.com/api/"

    # Alternative endpoints
    US1_ENDPOINT = "https://api.us1.sumologic.com/api/"
    US2_ENDPOINT = "https://api.us2.sumologic.com/api/"
    EU_ENDPOINT = "https://api.eu.sumologic.com/api/"
    AU_ENDPOINT = "https://api.au.sumologic.com/api/"

def get_sumo_client():
    """Initialize Sumo Logic API client"""
    sumo = SumoLogic(
        accessId='suPROD98765432101',
        accessKey='fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321',
        endpoint='https://api.sumologic.com/api/'
    )
    return sumo

def send_logs_to_http_source():
    """Send logs to HTTP source endpoint"""
    import requests

    http_source_url = "https://collectors.sumologic.com/receiver/v1/http/ZXhhbXBsZV9odHRwX3NvdXJjZV90b2tlbl8xMjM0NTY3ODkw"

    log_data = {
        "timestamp": "2026-04-21T12:00:00Z",
        "level": "INFO",
        "message": "Application started successfully"
    }

    response = requests.post(http_source_url, json=log_data)
    return response

# Environment-based configuration
SUMO_CONFIG = {
    'access_id': os.getenv('SUMO_ACCESS_ID', 'suDEFAULT12345678'),
    'access_key': os.getenv('SUMO_ACCESS_KEY', 'default1234567890abcdef1234567890abcdef1234567890abcdef1234567890'),
    'endpoint': os.getenv('SUMO_ENDPOINT', 'https://api.sumologic.com/api/')
}

# Multiple environment setup
ENVIRONMENTS = {
    'production': {
        'access_id': 'suPROD98765432101',
        'access_key': 'fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321',
        'endpoint': 'https://api.us2.sumologic.com/api/',
        'http_source': 'https://collectors.sumologic.com/receiver/v1/http/cHJvZF9odHRwX3NvdXJjZV90b2tlbg=='
    },
    'staging': {
        'access_id': 'suSTAG9012345678WXYZ',
        'access_key': '1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
        'endpoint': 'https://api.us1.sumologic.com/api/',
        'http_source': 'https://endpoint1.collection.us1.sumologic.com/receiver/v1/http/c3RhZ2luZ19odHRwX3NvdXJjZQ=='
    }
}

# Collector configuration
COLLECTOR_CONFIG = {
    'name': 'python-app-collector',
    'installation_token': 'suTOKEN5678901234ABCD8901EFGH2345IJKL6789MNOP',
    'sources': [
        {
            'name': 'application-logs',
            'sourceType': 'HTTP',
            'url': 'https://collectors.sumologic.com/receiver/v1/http/YXBwbGljYXRpb25fbG9nc19zb3VyY2VfdG9rZW4='
        }
    ]
}
