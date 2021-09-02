#!/usr/local/bin/python

import os
import sys
import shutil
from importlib import import_module

script_path = sys.argv[1]
if not os.path.exists(script_path):
    print("script(" + script_path + ") does not exist!")
    sys.exit(1)

print("loading script from " + script_path)
shutil.copy(script_path, "./script.py")

script = import_module("script")

print("execure script")
output = sys.argv[2]
script.generate(output)
