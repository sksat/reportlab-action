import sys
import shutil
from importlib import import_module

script_path = sys.argv[1]
print("loading script from " + script_path)
shutil.copy(script_path, "./script.py")

script = import_module("script")

print("execure script")
script.generate(sys.argv[2])
