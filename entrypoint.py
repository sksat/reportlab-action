#!/usr/local/bin/python

import os
import sys
import shutil
from importlib import machinery

script_path = sys.argv[1]
if not os.path.exists(script_path):
    print("script(" + script_path + ") does not exist!")
    sys.exit(1)

print("loading script from " + script_path)

loader = machinery.SourceFileLoader('.', script_path)
script = loader.load_module()

print("execure script")
output = sys.argv[2]
script.generate(output)
