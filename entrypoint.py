import sys
from importlib import import_module

script = import_module(sys.argv[1])
script.generate(sys.argv[2])
