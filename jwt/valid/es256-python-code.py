# Metadata:
# label: JWT Token (ES256) in Python code
# type: jwt
# algorithm: ES256
# context: Python source code
# generator: manual

import requests

class APIClient:
    def __init__(self):
        # JWT token signed with ES256 (ECDSA with P-256 curve)
        self.access_token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtleS0yMDI0LTAxIn0.eyJzdWIiOiJ1c2VyMTIzNCIsIm5hbWUiOiJKYW5lIFNtaXRoIiwiZW1haWwiOiJqYW5lQGV4YW1wbGUuY29tIiwiaWF0IjoxNzA5MzIwMDAwLCJleHAiOjE3MDkzMjM2MDAsInNjb3BlIjoidXNlcjpyZWFkIHVzZXI6d3JpdGUifQ.9xJl3K8mN6pQ2rS5tU7vW0xY1zA3bC4dE5fG6hI8jK9lM1nO2pQ3rS4tU6vW7xY8zA9bC0dE1fG2hI3jK4lM5nO"

        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def get_user_profile(self):
        response = requests.get(
            "https://api.example.com/user/profile",
            headers=self.headers
        )
        return response.json()
