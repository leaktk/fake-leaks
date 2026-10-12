# Metadata: label=Splunk SDK credentials in Python, type=api_key, provider=splunk, context=Python code, generator=manual

import splunklib.client as client
import splunklib.results as results
import requests
import os

class SplunkConfig:
    # Splunk Enterprise connection
    HOST = "splunk.example.com"
    PORT = 8089
    USERNAME = "admin"
    PASSWORD = "Spl@nk_Adm1n_P@ss_2026!"

    # Splunk Cloud connection
    CLOUD_HOST = "prd-p-xyz789.splunkcloud.com"
    CLOUD_TOKEN = "eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIifQ.eyJpc3MiOiJjbG91ZF91c2VyIn0.W3hY5zA6bC7dE8fG9hI0jK1lM2nO3pQ4rS5tU6vW7xY8zA"

def get_splunk_service():
    """Connect to Splunk Enterprise"""
    service = client.connect(
        host='splunk.example.com',
        port=8089,
        username='api_user',
        password='API_Us3r_Spl@nk_P@ss!',
        scheme='https'
    )
    return service

def get_splunk_cloud_service():
    """Connect to Splunk Cloud with token"""
    service = client.connect(
        host='prd-p-xyz789.splunkcloud.com',
        port=8089,
        token='eyJraWQiOiJzcGx1bmsuc2VjcmV0LmNsb3VkIiwiYWxnIjoiSFM1MTIifQ.eyJpc3MiOiJjbG91ZF9hZG1pbiJ9.5zA6bC7dE8fG9hI0jK1lM',
        scheme='https'
    )
    return service

def send_to_hec():
    """Send events to HTTP Event Collector"""
    hec_url = "https://splunk-hec.example.com:8088/services/collector/event"
    hec_token = "5f6a7b8c-9d0e-1f2a-3b4c-5d6e7f8a9b0c"

    headers = {
        "Authorization": f"Splunk {hec_token}",
        "Content-Type": "application/json"
    }

    event = {
        "event": {
            "message": "Application event",
            "severity": "INFO"
        },
        "sourcetype": "application:log",
        "index": "main"
    }

    response = requests.post(hec_url, json=event, headers=headers, verify=True)
    return response

# Environment-based configuration
SPLUNK_ENV_CONFIG = {
    'host': os.getenv('SPLUNK_HOST', 'splunk.example.com'),
    'port': int(os.getenv('SPLUNK_PORT', '8089')),
    'username': os.getenv('SPLUNK_USERNAME', 'default_user'),
    'password': os.getenv('SPLUNK_PASSWORD', 'D3f@ult_Spl@nk_P@ss!'),
    'token': os.getenv('SPLUNK_TOKEN', None)
}

# HEC configuration for multiple environments
HEC_CONFIGS = {
    'production': {
        'url': 'https://prod-hec.splunkcloud.com:8088/services/collector',
        'token': '1bC2dE3f-G4hI-5jK6-lM7n-O8pQ9rS0tU1v',
        'index': 'prod_logs'
    },
    'staging': {
        'url': 'https://staging-hec.example.com:8088/services/collector',
        'token': '9d0e1f2a-3b4c-5d6e-7f8a-9b0c1d2e3f4a',
        'index': 'staging_logs'
    },
    'development': {
        'url': 'https://dev-hec.example.com:8088/services/collector',
        'token': '3f4a5b6c-7d8e-9f0a-1b2c-3d4e5f6a7b8c',
        'index': 'dev_logs'
    }
}

# Forwarder configuration
FORWARDER_CONFIG = {
    'deployment_server': 'deployment-server.example.com:8089',
    'deployment_user': 'forwarder_admin',
    'deployment_password': 'F0rw@rd3r_Adm1n_P@ss_2026!',
    'receiving_indexer': 'indexer.example.com:9997',
    'ssl_password': 'SSL_C3rt_P@ssw0rd_2026!'
}

# License master credentials
LICENSE_CONFIG = {
    'license_master': 'license-master.example.com:8089',
    'license_user': 'license_admin',
    'license_password': 'L1c3ns3_M@st3r_P@ss!',
    'license_key': 'ABCD-1234-EFGH-5678-IJKL-9012-MNOP-3456-QRST-7890'
}
