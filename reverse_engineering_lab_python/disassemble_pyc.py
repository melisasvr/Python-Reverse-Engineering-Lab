
import dis
import marshal
import sys
import types
from pathlib import Path


def disassemble_code(code: types.CodeType, depth: int = 0) -> None:
    indent = "    " * depth

    print(f"\n{indent}Function/code object: {code.co_name}")
    print(f"{indent}First source line: {code.co_firstlineno}")
    print(f"{indent}Constants: {code.co_consts}")
    print(f"{indent}Names: {code.co_names}")
    print(f"{indent}Instructions:")

    dis.dis(code)

    for const in code.co_consts:
        if isinstance(const, types.CodeType):
            disassemble_code(const, depth + 1)


def main() -> None:
    path = Path("build/demo_auth.pyc")

    if not path.is_file():
        print(f"File not found: {path.resolve()}")
        sys.exit(1)

    data = path.read_bytes()

    # Python 3.7+ .pyc files have a 16-byte header.
    if len(data) < 16:
        print("File is too small to be a valid modern .pyc file.")
        sys.exit(1)

    try:
        code = marshal.loads(data[16:])
    except (EOFError, ValueError, TypeError) as exc:
        print(f"Could not decode bytecode: {exc}")
        sys.exit(1)

    if not isinstance(code, types.CodeType):
        print("The compiled payload is not a Python code object.")
        sys.exit(1)

    print(f"File: {path.resolve()}")
    print(f"Size: {len(data)} bytes")
    print(f"Python version: {sys.version}")
    print("Note: marshal data should be inspected with a compatible Python version.")

    disassemble_code(code)


if __name__ == "__main__":
    main()
