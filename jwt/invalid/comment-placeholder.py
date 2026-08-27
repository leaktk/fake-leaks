# Metadata: label=JWT placeholder in comments, type=jwt, context=Python comments, generator=manual, valid=false

# This file contains JWT-like strings in comments that should not be flagged

def authenticate(token):
    """
    Authenticate user with JWT token.

    Example token format: eyJhbGc...payload...signature
    Replace with your actual JWT token: your-jwt-token-here
    """
    # TODO: Replace this placeholder: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example.placeholder

    if token == "":
        raise ValueError("Token cannot be empty")

    return True

# Example usage:
# token = "eyJ..." # Put your JWT here
