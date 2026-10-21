
import sys
from demo_auth import validate_credentials


def trace_calls(frame, event, arg):
    if frame.f_code is validate_credentials.__code__:
        if event == "line":
            print(
                f"Executing line {frame.f_lineno}: "
                f"{frame.f_code.co_name}"
            )
    return trace_calls


cases = [
    ("ab", "wrong-password"),
    ("melisa", "1234567"),
    ("wrong-user", "blue-orbit-42"),
    ("melisa", "blue-orbit-42"),
]

sys.settrace(trace_calls)

try:
    for username, password in cases:
        print(f"\nTesting username={username!r}")
        result = validate_credentials(username, password)
        print("Result:", result)
finally:
    sys.settrace(None)
