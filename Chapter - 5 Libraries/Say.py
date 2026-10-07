import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex(f"Hello, {sys.argv[1]}")