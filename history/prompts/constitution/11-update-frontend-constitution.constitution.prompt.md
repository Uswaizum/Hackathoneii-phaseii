---
id: 11
title: Update Frontend Constitution
stage: constitution
date: 2026-01-16
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: 003-auth-jwt-verification
user: s.c
command: /sp.constitution
labels: [constitution, frontend, authentication, security]
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
Spec: Frontend Web Application & UX

Core principles:
- API-driven UI (frontend is a pure client of the backend)
- Secure-by-default (no unauthenticated API access)
- Responsive and accessible design
- Clear separation between UI, state, and API logic

Key standards:
- All data must come from backend APIs
- JWT token must be attached to every request
- UI must reflect real backend state (no mock data)
- Components must be reusable and composable

Constraints:
- Use Next.js App Router (16+)
- TypeScript is mandatory
- Tailwind CSS for styling
- No direct database access
- No business logic duplication from backend

Success criteria:
- Users can sign up, sign in, and sign out
- Users can fully manage their tasks via UI
- UI is responsive and usable on mobile and desktop
- Auth and task state remain consistent across refreshes

## Response snapshot

Updated the project constitution to version 1.3.0, incorporating the new frontend web application and UX requirements. Added four new principles (API-Driven UI, Secure-by-Default Design, Responsive and Accessible Design, Frontend Separation) and updated constraints and success criteria to reflect the frontend requirements. The constitution now properly reflects all frontend development standards and requirements provided.

## Outcome

- ✅ Impact: Updated constitution with frontend requirements, version bumped to 1.3.0
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md updated with new frontend content
- 🔁 Next prompts: Proceed with frontend implementation following new constitution
- 🧠 Reflection: Constitution now fully covers frontend development requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard constitution update
- Next experiment (smallest change to try): implement Next.js frontend per constitution