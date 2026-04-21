// Metadata: label=False positive - JWT-like method call, type=jwt, context=Java code, generator=manual, valid=false

// This should NOT be flagged as a JWT token - it's a method call

public class TokenValidator {
    public boolean validateToken(String token) {
        // Method call that looks like base64 but isn't a JWT
        return foreignKeyJsonObject.get("header").toString()
            .equals(headerValue.toString());
    }

    // Another false positive - variable names
    String jwtExample = "eyJ...example...placeholder";
    String tokenPlaceholder = "your.jwt.token.here";
}
