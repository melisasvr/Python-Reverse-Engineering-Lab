"""Compile demo_auth.py to Python bytecode using the active Python interpreter."""
import py_compile
from pathlib import Path

root = Path(__file__).resolve().parent
output = root / "build" / "demo_auth.pyc"
output.parent.mkdir(parents=True, exist_ok=True)
py_compile.compile(
    str(root / "demo_auth.py"),
    cfile=str(output),
    doraise=True,
    optimize=0,
)
print(f"Created: {output}")
print("Use the same Python version to inspect this bytecode.")
