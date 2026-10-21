# Python Reverse Engineering Lab

A small Python authentication demo intended for learning how to inspect a program without first relying on its source code.

## Files

- `demo_auth.py` — readable source code.
- `build_bytecode.py` — generates a `.pyc` bytecode file for inspection.
- `tests/test_demo_auth.py` — basic behavior tests.
- `requirements.txt` — no third-party packages required.

## Run the program

Requires Python 3.10+.

```bash
python demo_auth.py
```

Demo credentials:
- Username: `melisa`
- Password: `blue-orbit-42`

This is intentionally insecure training code. Do not use embedded credentials for real authentication.

## Create Python bytecode

```bash
python build_bytecode.py
```

This writes `build/demo_auth.pyc`. Python `.pyc` files are bytecode caches, not standalone native executables. Their format and bytecode instructions depend on the Python version. Use the same Python version when compiling and inspecting.

## First investigation

1. Keep the source code aside.
2. Open `build/demo_auth.pyc` in a Python bytecode/disassembly tool, or inspect it with Python's built-in `dis` module.
3. Find the functions corresponding to `main`, `validate_credentials`, and `show_result`.
4. Identify:
   - the minimum accepted username and password lengths;
   - the embedded credential strings;
   - the branches that lead to success or failure;
   - the exit code returned by `main`.
5. Write down what you observed, then compare it with `demo_auth.py`.

To disassemble the bytecode with the standard library:

```bash
python -m dis build/demo_auth.pyc
```

Depending on Python version, `python -m dis` may not directly accept a `.pyc` file. If it does not, use this small helper:

```bash
python -c "import marshal,dis; f=open('build/demo_auth.pyc','rb'); f.read(16); dis.dis(marshal.loads(f.read()))"
```

The 16-byte header is typical for modern CPython versions; header size can vary by Python version. If the helper fails, load the file with the matching Python version and inspect its header.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Limitations

Python bytecode is much higher-level than native machine code and is version-specific. If you want to practice native executable reverse engineering later, this same feature can be ported to C or Rust and compiled to an ELF/PE binary.
