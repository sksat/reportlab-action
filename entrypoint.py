import sys
from importlib import import_module

script = import_module(sys.argv[1])
output = script.generate()

with open(sys.argv[2], "wb") as f:
    output.write(f)
