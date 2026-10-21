import dis
import marshal
from pathlib import Path
from types import CodeType

path = Path("build/demo_auth.pyc")
data = path.read_bytes()

code = marshal.loads(data[16:])

def inspect_functions(obj):
    for item in obj.co_consts:
        if isinstance(item, CodeType):
            print("\n" + "=" * 60)
            print("Function:", item.co_name)
            print("First line:", item.co_firstlineno)
            print("Constants:", item.co_consts)
            print("Names:", item.co_names)
            print("\nDisassembly:")
            dis.dis(item)
            inspect_functions(item)

inspect_functions(code)