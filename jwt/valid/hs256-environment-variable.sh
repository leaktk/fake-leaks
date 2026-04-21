# Metadata:
# label: JWT Token (HS256) in environment variable
# type: jwt
# algorithm: HS256
# context: shell script / environment variable
# generator: manual

#!/bin/bash

# Export JWT token as environment variable
export JWT_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Use in API call
curl -H "Authorization: Bearer $JWT_TOKEN" https://api.example.com/user
