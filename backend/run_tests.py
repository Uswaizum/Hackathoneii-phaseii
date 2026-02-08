#!/usr/bin/env python3
"""
Simple test runner for the API endpoints.
This script validates that all API functionality works as expected.
"""

import subprocess
import sys
import os

def run_tests():
    """Run the API tests."""
    print("Running API tests...\n")

    # Change to backend directory
    os.chdir('backend')

    # Run the test file directly
    result = subprocess.run([sys.executable, 'test_api.py'], capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout)
        print("\n✅ All tests passed successfully!")
        return True
    else:
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("\n❌ Tests failed!")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)