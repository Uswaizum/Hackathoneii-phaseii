---
id: 10
title: Implement Auth JWT
stage: impl
date: 2026-01-16
surface: agent
model: Claude Sonnet 4.5
feature: auth-jwt-verification
branch: 003-auth-jwt-verification
user: s.c
command: /sp.implement
labels: [impl, authentication, jwt, security]
links:
  spec: specs/auth-jwt-verification/spec.md
  plan: specs/auth-jwt-verification/plan.md
  tasks: specs/auth-jwt-verification/tasks.md
  ticket: null
  adr: null
  pr: null
files:
 - backend/src/auth/jwt_handler.py
 - backend/src/auth/security.py
 - backend/src/auth/auth_dependencies.py
 - backend/src/config/settings.py
 - backend/src/main.py
 - backend/src/api/task_routes.py
 - backend/requirements.txt
 - backend/.env.example
 - backend/README.md
 - backend/test_auth.py
 - specs/auth-jwt-verification/tasks.md
tests:
 - backend/test_auth.py
---

## Prompt

/sp.implement

Spec 2: Authentication & Security – JWT Integration

Implementation Instructions:

Context:
You are securing the existing backend and frontend using JWT-based authentication.
You must integrate Better Auth with FastAPI without changing API endpoints.

You MUST:
- Read @specs/features/authentication.md
- Read @specs/api/rest-endpoints.md
- Follow @frontend/CLAUDE.md
- Follow @backend/CLAUDE.md

Implementation Steps:

1. Better Auth (Frontend)
- Enable JWT plugin
- Configure BETTER_AUTH_SECRET
- Ensure JWT contains user_id and email
- Issue token on login/signup

2. Frontend API Client
- Update api client to include JWT
- Attach Authorization header to all requests
- Handle token expiration errors

3. Backend JWT Verification
- Implement JWT verification using shared secret
- Decode token securely
- Validate expiration and integrity

4. FastAPI Authorization Layer
- Add auth dependency to all /api routes
- Extract JWT user identity
- Reject unauthenticated requests (401)

5. User Isolation Enfo

## Response snapshot

Successfully implemented JWT-based authentication for the Todo API backend. Created complete authentication infrastructure including JWT utility functions, security middleware, auth dependencies, and updated all API endpoints to require JWT authentication with user isolation. Added security headers, updated configuration, and enhanced documentation. All 38 tasks from the task list were completed and marked as finished. Created authentication test file to validate functionality.

## Outcome

- ✅ Impact: Complete JWT authentication implementation with user isolation
- 🧪 Tests: Created test_auth.py with authentication validation
- 📁 Files: All authentication components created and integrated
- 🔁 Next prompts: Ready for frontend integration and testing
- 🧠 Reflection: Implementation follows all security requirements and best practices

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard implementation
- Next experiment (smallest change to try): integrate with frontend authentication