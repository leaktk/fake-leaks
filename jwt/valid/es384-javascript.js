// Metadata:
// label: JWT Token (ES384) in JavaScript
// type: jwt
// algorithm: ES384
// context: JavaScript source code
// generator: manual

const express = require('express');
const app = express();

// JWT token for service-to-service authentication (ES384)
const SERVICE_TOKEN = 'eyJhbGciOiJFUzM4NCIsInR5cCI6IkpXVCIsImtpZCI6ImVzLWtleS0zODQtMDEifQ.eyJzdWIiOiJwYXltZW50LXNlcnZpY2UiLCJhdWQiOiJ1c2VyLXNlcnZpY2UiLCJpc3MiOiJhdXRoLnNlcnZpY2UubG9jYWwiLCJpYXQiOjE3MDkzMjAwMDAsImV4cCI6MTc0MDg1NjAwMCwic2NvcGUiOlsicmVhZDp1c2VycyIsIndyaXRlOnBheW1lbnRzIl0sInNlcnZpY2VfaWQiOiJwYXltZW50LXYyIn0.rX5yZ6aB7cD8eF9gH0iJ1kL2mN3oP4qR5sT6uV7wX8yZ9aB0cD1eF2gH3iJ4kL5mN6oP7qR8sT9uV';

// Middleware to add auth header
app.use((req, res, next) => {
    req.headers['X-Service-Token'] = SERVICE_TOKEN;
    next();
});

// API call with JWT in cookie
app.get('/api/user', (req, res) => {
    const userJWT = req.cookies.session_token || 'eyJhbGciOiJFUzM4NCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyXzEyMzQ1IiwibmFtZSI6IkFsaWNlIFdvbmRlcmxhbmQiLCJlbWFpbCI6ImFsaWNlQGV4YW1wbGUuY29tIiwiaWF0IjoxNzA5MzIwMDAwLCJleHAiOjE3MDkzMjM2MDAsInJvbGUiOiJ1c2VyIn0.sU6vW7xY8zA9bC0dE1fG2hI3jK4lM5nO6pQ7rS8tU9vW0xY1zA2bC3dE4fG5hI6jK7lM8nO9pQ';

    res.json({ token: userJWT });
});

app.listen(3000);
