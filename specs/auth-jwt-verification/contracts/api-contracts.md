# API Contracts: Authentication & Security – JWT-Based User Verification

## Overview
All existing API endpoints now require JWT authentication. The authentication layer sits between the client and existing endpoints, validating JWT tokens before forwarding requests.

## Authentication Requirements
All endpoints under `/api/*` now require a valid JWT token in the Authorization header.

### Authorization Header Format
```
Authorization: Bearer <jwt-token>
```

## Error Responses

### 401 Unauthorized
Returned when:
- No Authorization header is provided
- Authorization header is malformed
- JWT token is invalid (wrong signature)
- JWT token has expired
- JWT token is malformed

**Response Body**:
```json
{
  "detail": "Not authenticated",
  "error_code": "AUTH_001"
}
```

### 403 Forbidden (Future Enhancement)
Returned when:
- JWT is valid but user doesn't have permission for specific resource
- User tries to access resources belonging to other users

**Response Body**:
```json
{
  "detail": "Insufficient permissions",
  "error_code": "AUTH_002"
}
```

## Modified Endpoints

All existing endpoints from the Task Management API now require authentication:

### 1. Create Task (Protected)
- **Method**: `POST`
- **Endpoint**: `/api/{user_id}/tasks`
- **Authorization**: Requires valid JWT with matching user_id
- **Headers**: `Authorization: Bearer <token>`
- **Response Codes**:
  - `201 Created`: Task successfully created (with valid JWT)
  - `401 Unauthorized`: Invalid or missing JWT
  - `404 Not Found`: User not found or does not match JWT user_id

### 2. Get All Tasks (Protected)
- **Method**: `GET`
- **Endpoint**: `/api/{user_id}/tasks`
- **Authorization**: Requires valid JWT with matching user_id
- **Headers**: `Authorization: Bearer <token>`
- **Response Codes**:
  - `200 OK`: Successfully retrieved tasks (with valid JWT)
  - `401 Unauthorized`: Invalid or missing JWT

### 3. Get Task by ID (Protected)
- **Method**: `GET`
- **Endpoint**: `/api/{user_id}/tasks/{id}`
- **Authorization**: Requires valid JWT with matching user_id
- **Headers**: `Authorization: Bearer <token>`
- **Response Codes**:
  - `200 OK`: Task successfully retrieved (with valid JWT)
  - `401 Unauthorized`: Invalid or missing JWT
  - `404 Not Found`: Task not found or does not belong to user

### 4. Update Task (Protected)
- **Method**: `PUT`
- **Endpoint**: `/api/{user_id}/tasks/{id}`
- **Authorization**: Requires valid JWT with matching user_id
- **Headers**: `Authorization: Bearer <token>`
- **Response Codes**:
  - `200 OK`: Task successfully updated (with valid JWT)
  - `401 Unauthorized`: Invalid or missing JWT
  - `404 Not Found`: Task not found or does not belong to user

### 5. Delete Task (Protected)
- **Method**: `DELETE`
- **Endpoint**: `/api/{user_id}/tasks/{id}`
- **Authorization**: Requires valid JWT with matching user_id
- **Headers**: `Authorization: Bearer <token>`
- **Response Codes**:
  - `204 No Content`: Task successfully deleted (with valid JWT)
  - `401 Unauthorized`: Invalid or missing JWT
  - `404 Not Found`: Task not found or does not belong to user

### 6. Toggle Task Completion (Protected)
- **Method**: `PATCH`
- **Endpoint**: `/api/{user_id}/tasks/{id}/complete`
- **Authorization**: Requires valid JWT with matching user_id
- **Headers**: `Authorization: Bearer <token>`
- **Response Codes**:
  - `200 OK`: Task completion status updated (with valid JWT)
  - `401 Unauthorized`: Invalid or missing JWT
  - `404 Not Found`: Task not found or does not belong to user

## Token Validation Endpoints (New)

### Validate Token
- **Method**: `POST`
- **Endpoint**: `/auth/validate`
- **Description**: Validates a JWT token and returns user information
- **Headers**: `Authorization: Bearer <token>`
- **Response Codes**:
  - `200 OK`: Token is valid
  - `401 Unauthorized`: Token is invalid
- **Success Response**:
```json
{
  "valid": true,
  "user_id": "string",
  "expires_at": "datetime"
}
```

## Security Headers
All responses will include appropriate security headers:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`