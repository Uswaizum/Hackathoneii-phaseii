<!-- SYNC IMPACT REPORT
Version change: 1.2.0 → 1.3.0
Modified principles:
  - IX. JWT Security Standards (expanded to include frontend integration requirements)
Added sections:
  - X. API-Driven UI Principle
  - XI. Secure-by-Default Design Principle
  - XII. Responsive and Accessible Design Principle
  - XIII. Frontend Separation Principle
Removed sections: None
Templates requiring updates:
  - ✅ .specify/templates/plan-template.md (to be checked)
  - ✅ .specify/templates/spec-template.md (to be checked)
  - ✅ .specify/templates/tasks-template.md (to be checked)
Follow-up TODOs: None
-->
# Hackathon II – Phase II Todo Full-Stack Web Application Constitution

## Core Principles

### I. Spec-Driven Development
Implementation must strictly follow written specs. All development work must be traceable to explicit requirements documented in specification files. No feature or change may be implemented without prior specification approval. This ensures deterministic and predictable development outcomes.

### II. Deterministic Backend Behavior
Backend services must exhibit deterministic behavior: same input must always produce same output. This principle ensures reliability, testability, and user trust in the system. All operations must be idempotent and reproducible.

### III. Data Integrity and User Isolation
Data integrity must be maintained at all times. All data operations must be scoped to specific user contexts to ensure proper isolation and prevent cross-user contamination. Tasks are always scoped to a user_id to maintain data boundaries.

### IV. Production-Grade API Design
All API endpoints must follow RESTful design principles and production-grade standards. All API endpoints must match the defined REST contract. APIs must be well-documented, versioned, and maintain backward compatibility where feasible. All responses must be JSON serializable and errors must use proper HTTP status codes.

### V. SQLModel ORM Standard
SQLModel must be the exclusive ORM used for all database operations. This ensures consistency, reduces complexity, and leverages SQLModel's type safety and validation capabilities. Database schema must be explicitly defined and migrated.

### VI. Stateless Backend Architecture
The backend must be completely stateless. All state must be stored in the database or client-side. No session data may be stored server-side to ensure horizontal scalability and fault tolerance. Backend must be stateless with environment-based configuration only (no hardcoded secrets).

### VII. JWT Authentication Implementation
The system must implement JWT-based authentication for all protected endpoints. All sensitive configuration must be externalized to environment variables, and the architecture must support user-scoped operations. JWTs must be verified cryptographically on the backend with no trust placed in frontend without token verification.

### VIII. Zero-Trust Authentication Principle
Backend must operate on a zero-trust model where every request must be authenticated. No endpoint should be considered secure without proper authentication verification. User identity must come only from decoded JWT claims, never from client-provided values.

### IX. JWT Security Standards
The backend must implement stateless authentication using JWT with strong cryptographic verification. JWT expiration must be enforced, and the backend must not rely on session-based authentication. All protected endpoints require a valid JWT token. Frontend must securely store and transmit JWT tokens to backend APIs.

### X. API-Driven UI Principle
The frontend must act as a pure client of the backend API. All data must come from backend APIs and the UI must reflect real backend state with no mock data. The frontend should not duplicate business logic from the backend.

### XI. Secure-by-Default Design Principle
The frontend must implement security measures by default. No unauthenticated API access should be allowed. All requests to backend APIs must include proper authentication tokens.

### XII. Responsive and Accessible Design Principle
The frontend must be designed to work across all device sizes (mobile, tablet, desktop) with responsive layouts. The UI must be accessible to users with disabilities following WCAG guidelines.

### XIII. Frontend Separation Principle
There must be a clear separation between UI components, application state management, and API communication logic. Components must be reusable and composable to promote maintainability.

## Key Standards

### API Contract Compliance
- All API endpoints must match the defined REST contract exactly
- All responses must be JSON serializable
- Proper HTTP status codes must be used for all responses
- Errors must follow consistent error response formats

### Database and Schema Management
- Database schema must be explicitly defined and version-controlled
- All schema changes must go through proper migration procedures
- Data persistence must be implemented using Neon PostgreSQL
- All tasks are always scoped to a user_id for proper isolation

### Frontend Development Standards
- All data must come from backend APIs
- JWT token must be attached to every API request
- UI must reflect real backend state (no mock data)
- Components must be reusable and composable
- Use Next.js App Router (16+)
- TypeScript is mandatory
- Tailwind CSS for styling

### Security and Configuration
- Environment-based configuration only (no hardcoded secrets)
- All protected endpoints require a valid JWT
- JWT must be verified cryptographically on the backend
- Backend must not trust frontend without token verification
- User identity must come only from decoded JWT claims
- No direct database access from frontend
- No business logic duplication from backend in frontend
- No manual coding outside Claude Code tooling

## Constraints

### Development Constraints
- No manual coding outside Claude Code tooling
- All changes must be made through approved automation tools
- No direct file editing without proper tooling and tracking

### Architectural Constraints
- Backend must remain stateless at all times
- No persistent local storage - all data must go through database
- No caching layers that could introduce state inconsistencies
- Environment-based configuration only (no hardcoded secrets)
- Better Auth is frontend-only (Next.js)
- FastAPI backend must not depend on Better Auth runtime
- Shared secret must be provided via environment variables
- No session-based authentication allowed
- No direct database access from frontend
- No business logic duplication from backend in frontend

## Success Criteria

### Functional Requirements
- CRUD operations fully functional for all entities
- Data persists in Neon PostgreSQL
- Tasks are always scoped to a user_id for proper user isolation
- All data operations properly scoped to user contexts
- Users can sign up, sign in, and sign out
- Users can fully manage their tasks via UI

### Quality Requirements
- Unauthorized requests return 401
- Authenticated users can only access their own tasks
- JWT expiration is enforced
- Backend is fully stateless and secure
- API endpoints pass basic manual testing via curl or frontend
- All operations maintain data integrity
- System handles concurrent operations safely
- Deterministic backend behavior maintained (same input → same output)
- UI is responsive and usable on mobile and desktop
- Auth and task state remain consistent across refreshes

## Governance

This Constitution represents the supreme governing document for the Hackathon II – Phase II Todo Full-Stack Web Application project. All development work, architectural decisions, and implementation details must comply with these principles.

### Amendment Process
- All amendments must be documented with clear rationale
- Changes must be approved through the established review process
- Migration plans must be provided for any breaking changes
- Version increments must follow semantic versioning rules

### Compliance Requirements
- All pull requests and code reviews must verify compliance
- Any deviations must be explicitly justified and documented
- Complexity introductions must be approved by project architects
- Use this constitution as the primary guidance for all development decisions

**Version**: 1.3.0 | **Ratified**: 2026-01-15 | **Last Amended**: 2026-01-16
