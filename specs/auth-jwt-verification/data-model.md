# Data Model: Authentication & Security – JWT-Based User Verification

## JWT Token Entity

### Claims Structure
- **user_id**: String (Required) - Unique identifier for the user from JWT claims
- **email**: String (Optional) - User's email address from JWT claims
- **exp**: Integer (Required) - Unix timestamp for token expiration
- **iat**: Integer (Required) - Unix timestamp for token issuance
- **sub**: String (Optional) - Subject identifier for the token
- **iss**: String (Optional) - Issuer of the token

### Validation Rules
- **Signature Verification**: Token signature must match configured shared secret
- **Expiration Check**: Current time must be before exp claim
- **Issuance Validation**: Token must not be issued in the future
- **User Context Matching**: user_id in token must match user context in request URL

### State Transitions
- **Valid Token**: Token passes all validation checks
- **Expired Token**: Current time exceeds exp claim
- **Invalid Signature**: Token signature doesn't match shared secret
- **Malformed Token**: Token structure doesn't conform to JWT standards

## Authorization Context Entity

### Fields
- **authenticated_user_id**: String (Required) - User ID extracted from valid JWT
- **is_authenticated**: Boolean (Required) - Whether the JWT is valid
- **token_scopes**: List[String] (Optional) - Scopes granted by the token
- **valid_until**: DateTime (Required) - When the token expires

## Security Validation Entity

### Fields
- **request_endpoint**: String (Required) - API endpoint being accessed
- **expected_user_id**: String (Required) - User ID expected for this request
- **actual_user_id**: String (Required) - User ID from JWT claims
- **validation_result**: String (Required) - Result of authorization check
- **access_granted**: Boolean (Required) - Whether access was granted