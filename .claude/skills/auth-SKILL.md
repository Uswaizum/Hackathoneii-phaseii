name: authentication
description: Implement secure user signup and signin using Better Auth, manage password hashing, and issue/verify JWT tokens for authenticated API access.

---

# Authentication Implementation

## Instructions

1. **Signup & Signin**
   - Implement user registration and login using Better Auth
   - Rely on Better Auth for secure password hashing
   - Handle login, logout, and session lifecycle

2. **JWT Token Handling**
   - Enable JWT issuance in Better Auth
   - Include user identifiers in token payload
   - Set token expiration and signing secret
   - Attach JWT to API requests (`Authorization: Bearer`)

3. **Frontend Integration**
   - Integrate auth flows with Next.js App Router
   - Protect authenticated routes
   - Redirect unauthenticated users appropriately

4. **Backend Verification**
   - Verify JWT tokens in FastAPI
   - Decode token to extract authenticated user
   - Reject invalid or expired tokens
   - Enforce user-level access control

## Best Practices
- Use environment variables for shared secrets
- Never store or log plain-text passwords
- Treat backend as zero-trust: always verify JWT
- Return proper auth error codes (401, 403)
- Follow specs under `/specs/features/authentication.md`

## Example Structure
```ts
// Frontend
const session = await auth.signIn({ email, password })
const token = session.jwt

