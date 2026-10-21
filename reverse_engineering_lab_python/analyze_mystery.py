
import dis
import marshal
import py_compile
import types
from pathlib import Path

source = Path("mystery_target.py")
compiled = Path("build/mystery_target.pyc")

compiled.parent.mkdir(exist_ok=True)
py_compile.compile(
    str(source),
    cfile=str(compiled),
    doraise=True,
)

data = compiled.read_bytes()
code = marshal.loads(data[16:])

def inspect(code_object):
    if code_object.co_name == "evaluate":
        print("Function:", code_object.co_name)
        print("Constants:", code_object.co_consts)
        print("Names:", code_object.co_names)
        dis.dis(code_object)

    for item in code_object.co_consts:
        if isinstance(item, types.CodeType):
            inspect(item)

inspect(code)
