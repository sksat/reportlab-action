import sys
import shutil
from importlib import import_module

script_path = sys.argv[1]
shutil.copy(script_path, "./script.py")

script = import_module("script")
script.generate(sys.argv[2])
