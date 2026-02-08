# Quickstart Guide: Authentication & Security – JWT-Based User Verification

## Setup Instructions

### 1. Prerequisites
- Complete the Task Management API setup (Spec 1)
- Better Auth configured on the frontend
- Python 3.13+
- Pip package manager

### 2. Environment Setup
1. Navigate to the backend directory
2. Install additional authentication dependencies:
   ```bash
   pip install python-jose[cryptography] passlib[bcrypt] python-multipart
   ```

3. Update your `.env` file with JWT configuration:
   ```env
   DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/todo_db
   ENVIRONMENT=development
   LOG_LEVEL=info
   SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=1440  # 24 hours
   ```

### 3. Configuration
1. The authentication system will automatically validate JWT tokens
2. All existing API endpoints now require a valid JWT token
3. The token must contain a user_id that matches the user_id in the request URL

## API Usage Examples

### With Authentication (Correct Way)

#### Get Tasks with Valid JWT
```bash
curl -X GET http://localhost:8000/api/user123/tasks \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

#### Create Task with Valid JWT
```bash
curl -X POST http://localhost:8000/api/user123/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -d '{"title": "New task", "description": "With authentication"}'
```

### Without Authentication (Will Fail)

#### Attempt to Get Tasks without JWT (Will Return 401)
```bash
curl -X GET http://localhost:8000/api/user123/tasks
# Response: 401 Unauthorized
```

#### Attempt to Get Tasks with Invalid JWT (Will Return 401)
```bash
curl -X GET http://localhost:8000/api/user123/tasks \
  -H "Authorization: Bearer invalid.token.here"
# Response: 401 Unauthorized
```

## Frontend Integration

### Sending Requests with JWT
```javascript
// Example of how to include JWT in API requests
const makeAuthenticatedRequest = async (url, method = 'GET', data = null) => {
  const token = localStorage.getItem('jwt_token'); // or however you store the token

  const response = await fetch(url, {
    method,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    ...(data && { body: JSON.stringify(data) })
  });

  if (response.status === 401) {
    // Handle unauthorized - maybe redirect to login
    window.location.href = '/login';
    return;
  }

  return response;
};
```

## Testing Authentication

### Test Valid Token Access
1. Obtain a valid JWT token from Better Auth
2. Make requests with the `Authorization: Bearer <token>` header
3. Verify that you can access your own resources

### Test Invalid Token Access
1. Make requests with an invalid/expired token
2. Verify that you receive 401 Unauthorized responses

### Test User Isolation
1. Obtain a JWT token for user A
2. Try to access resources for user B
3. Verify that you receive 404 Not Found (not 401) to avoid revealing user existence

## Security Considerations

- JWT tokens are stateless and validated cryptographically
- User IDs in tokens are matched against URL parameters for authorization
- All API endpoints now require authentication
- Tokens expire after the configured time period
- Invalid tokens result in 401 Unauthorized responses

## Troubleshooting

- If getting 401 errors, verify your JWT token is valid and not expired
- If accessing other users' data, ensure the user_id in your token matches the URL
- Check that the Authorization header is formatted correctly: `Authorization: Bearer <token>`