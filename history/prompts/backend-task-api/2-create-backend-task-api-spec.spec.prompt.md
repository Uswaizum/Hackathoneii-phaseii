---
id: 2
title: Create Backend Task API Spec
stage: spec
date: 2026-01-16
surface: agent
model: Claude Sonnet 4.5
feature: backend-task-api
branch: 002-backend-task-api
user: s.c
command: /sp.specify
labels: [spec, backend, api, task-management]
links:
  spec: specs/backend-task-api/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/backend-task-api/spec.md
 - specs/backend-task-api/checklists/requirements.md
tests:
 - none
---

## Prompt

/sp.specify

Spec 1: Backend Core – Task Management API

Objective:
Build the backend foundation of the Todo application using FastAPI and SQLModel with persistent storage in Neon PostgreSQL.

Scope:
This spec covers database schema, models, and REST API endpoints for task management.
Authentication verification will be added in a later spec, but all data models and queries must already support user scoping.

Functional Requirements:

1. Database
- Use Neon Serverless PostgreSQL
- Use SQLModel ORM
- Define Task model with:
  - id (int, primary key)
  - user_id (string, indexed)
  - title (string, required, max 200 chars)
  - description (text, optional)
  - completed (boolean, default false)
  - created_at (timestamp)
  - updated_at (timestamp)

2. API Endpoints
Implement the following REST endpoints:

- GET /api/{user_id}/tasks
  - Returns all tasks for the given user_id

- POST /api/{user_id}/tasks
  - Creates a new task for the user

- GET /api/{user_id}/tasks/{id}
  - Returns task details

- PUT /api/{u

## Response snapshot

Created the feature specification for the Backend Core – Task Management API at specs/backend-task-api/spec.md. The specification includes user scenarios for creating, viewing, and updating tasks, functional requirements covering data storage and API functionality, and measurable success criteria. Also created a quality checklist at specs/backend-task-api/checklists/requirements.md to validate the specification.

## Outcome

- ✅ Impact: Created complete feature specification aligned with user requirements
- 🧪 Tests: none
- 📁 Files: specs/backend-task-api/spec.md and checklists/requirements.md created
- 🔁 Next prompts: Proceed to planning phase with /sp.plan
- 🧠 Reflection: Specification captures all essential user scenarios and requirements

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): standard spec creation
- Next experiment (smallest change to try): create implementation plan