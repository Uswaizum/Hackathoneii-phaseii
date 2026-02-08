---
id: 6
title: Update Authentication Constitution
stage: constitution
date: 2026-01-16
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: 002-backend-task-api
user: s.c
command: /sp.constitution
labels: [constitution, authentication, security]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

/sp.constitution

Project: Hackathon II – Phase II Todo Full-Stack Web Application
Spec: Authentication & Security Layer

Core principles:
- Zero-trust backend (every request must be authenticated)
- Stateless authentication using JWT
- Strong user isolation guarantees
- Security before convenience

Key standards:
- All protected endpoints require a valid JWT
- JWT must be verified cryptographically on the backend
- Backend must not trust frontend without token verification
- User identity must come only from decoded JWT claims

Constraints:
- Better Auth is frontend-only (Next.js)
- FastAPI backend must not depend on Better Auth runtime
- Shared secret must be provided via environment variables
- No session-based authentication allowed

Success criteria:
- Unauthorized requests return 401
- Authenticated users can only access their own tasks
- JWT expiration is enforced
- Backend is fully stateless and secure

## Response snapshot

Updated the project constitution to version 1.2.0, incorporating the new authentication and security requirements. Added new principles for Zero-Trust Authentication and JWT Security Standards, enhanced the JWT Authentication Implementation principle, and updated constraints and success criteria to reflect the authentication requirements. The constitution now properly reflects all security and authentication specifications provided.

## Outcome

- ✅ Impact: Updated constitution with authentication security requirements, version bumped to 1.2.0
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated with new security content
- 🔁 Next prompts: Proceed with authentication implementation following new constitution
- 🧠 Reflection: Constitution now fully covers JWT authentication and security requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard constitution update
- Next experiment (smallest change to try): implement JWT authentication middleware per constitution