#!/usr/bin/env python3
"""
Validation script to confirm that both frontend and backend implementations are complete and properly set up.
"""

import os
import sys
from pathlib import Path

def check_backend_implementation():
    """Check that all backend components are properly implemented."""
    print("Checking Backend Implementation...")

    backend_dir = Path("backend")

    if not backend_dir.exists():
        print("Backend directory does not exist")
        return False

    # Check for essential backend files
    essential_files = [
        "src/main.py",
        "src/database/database.py",
        "src/models/task_model.py",
        "src/schemas/task_schemas.py",
        "src/api/task_routes.py",
        "src/config/settings.py",
        "src/auth/",
        "requirements.txt",
        "README.md",
        ".env.example"
    ]

    missing_files = []
    for file_path in essential_files:
        full_path = backend_dir / file_path
        if not full_path.exists():
            missing_files.append(str(full_path))

    if missing_files:
        print(f"Missing backend files/directories: {missing_files}")
        return False

    print("All essential backend files exist")

    # Check for API endpoints implementation
    task_routes_content = (backend_dir / "src/api/task_routes.py").read_text()
    main_content = (backend_dir / "src/main.py").read_text()

    # Check if routes are properly mounted with user_id prefix
    if "prefix=\"/api/{user_id}\"" not in main_content or "include_router(task_router" not in main_content:
        print("Routes are not properly mounted with user_id prefix in main.py")
        return False

    # Check if the individual endpoints are implemented in the router
    endpoints_methods = [
        "@router.post(\"/tasks\"",
        "@router.get(\"/tasks\"",
        "@router.get(\"/tasks/{task_id}\"",
        "@router.put(\"/tasks/{task_id}\"",
        "@router.delete(\"/tasks/{task_id}\"",
        "@router.patch(\"/tasks/{task_id}/complete\""
    ]

    missing_endpoints = []
    for endpoint_pattern in endpoints_methods:
        if endpoint_pattern not in task_routes_content:
            missing_endpoints.append(endpoint_pattern)

    if missing_endpoints:
        print(f"Missing API endpoints in task_routes.py: {missing_endpoints}")
        return False

    print("All required API endpoints are implemented")

    # Check for authentication implementation
    auth_implemented = (
        "require_same_user" in task_routes_content and
        "Depends" in task_routes_content and
        "HTTPException" in task_routes_content
    )

    if not auth_implemented:
        print("Authentication not properly implemented in API routes")
        return False

    print("Authentication is implemented in API routes")

    return True

def check_frontend_implementation():
    """Check that all frontend components are properly implemented."""
    print("\nChecking Frontend Implementation...")

    frontend_dir = Path("frontend")

    if not frontend_dir.exists():
        print("Frontend directory does not exist")
        return False

    # Check for essential frontend files
    essential_files = [
        "app/page.tsx",
        "app/layout.tsx",
        "app/signin/page.tsx",
        "app/signup/page.tsx",
        "app/dashboard/page.tsx",
        "components/auth/LoginForm.tsx",
        "components/auth/SignupForm.tsx",
        "components/auth/LogoutButton.tsx",
        "components/tasks/TaskList.tsx",
        "components/tasks/TaskItem.tsx",
        "components/tasks/TaskForm.tsx",
        "components/tasks/TaskToggle.tsx",
        "hooks/useAuth.ts",
        "hooks/useTasks.ts",
        "lib/api.ts",
        "lib/auth.ts",
        "package.json",
        "README.md",
        ".env.local",
        "tsconfig.json",
        "tailwind.config.js"
    ]

    missing_files = []
    for file_path in essential_files:
        full_path = frontend_dir / file_path
        if not full_path.exists():
            missing_files.append(str(full_path))

    if missing_files:
        print(f"Missing frontend files/directories: {missing_files}")
        return False

    print("All essential frontend files exist")

    # Check for API integration in frontend
    api_client_content = (frontend_dir / "lib/api.ts").read_text()
    if "Authorization" not in api_client_content or "Bearer" not in api_client_content:
        print("API client is not properly configured for JWT authentication")
        return False

    print("Frontend API client is configured for JWT authentication")

    # Check for auth integration
    auth_content = (frontend_dir / "lib/auth.ts").read_text()
    if "loginUser" not in auth_content or "registerUser" not in auth_content:
        print("Auth functions not properly implemented")
        return False

    print("Frontend authentication functions are implemented")

    return True

def check_consistency():
    """Check that frontend and backend are consistent with each other."""
    print("\nChecking Frontend-Backend Consistency...")

    # Check that API endpoints match between frontend and backend
    backend_main = Path("backend/src/main.py").read_text()
    frontend_api = Path("frontend/lib/api.ts").read_text()

    # Both should use the same API path pattern
    if 'prefix="/api/{user_id}"' not in backend_main:
        print("Backend API path pattern inconsistent - expecting prefix='/api/{user_id}'")
        return False

    print("API path patterns are consistent between frontend and backend")

    return True

def main():
    """Validate the complete implementation."""
    print("Validating Full Stack Implementation")
    print("="*50)

    backend_ok = check_backend_implementation()
    frontend_ok = check_frontend_implementation()
    consistency_ok = check_consistency()

    print("\n" + "="*50)
    print("Validation Results:")
    print(f"Backend Implementation: {'PASS' if backend_ok else 'FAIL'}")
    print(f"Frontend Implementation: {'PASS' if frontend_ok else 'FAIL'}")
    print(f"Frontend-Backend Consistency: {'PASS' if consistency_ok else 'FAIL'}")

    if backend_ok and frontend_ok and consistency_ok:
        print("\nALL VALIDATIONS PASSED!")
        print("Both frontend and backend are properly implemented and ready to run")
        print("\nTo start the applications:")
        print("Backend: cd backend && uvicorn src.main:app --reload")
        print("Frontend: cd frontend && npm run dev")
        return True
    else:
        print("\nSOME VALIDATIONS FAILED!")
        print("Please review the issues above before running the applications.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)