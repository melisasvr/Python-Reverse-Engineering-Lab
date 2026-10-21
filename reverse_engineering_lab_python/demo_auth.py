#!/usr/bin/env python3
"""
Reverse Engineering Lab: Authentication Demo
For educational reverse-engineering practice only.

This deliberately insecure demo embeds credentials in the program so learners
can inspect Python bytecode and compare it with the source. Never use this
pattern for real authentication.
"""
from getpass import getpass


def validate_credentials(username: str, password: str) -> bool:
    """Return True when input lengths and the demo credentials match."""
    if len(username) <= 2:
        return False
    if len(password) <= 7:
        return False

    expected_username = "melisa"
    expected_password = "blue-orbit-42"

    if username != expected_username:
        return False
    if password != expected_password:
        return False
    return True


def show_result(valid: bool) -> None:
    """Print the result of the credential check."""
    if valid:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")


def main() -> int:
    print("=== Reverse Engineering Lab: Authentication Demo ===")
    username = input("Username: ")
    password = input("Password: ")

    valid = validate_credentials(username, password)
    show_result(valid)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
