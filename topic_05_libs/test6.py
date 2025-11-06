import cowsay
from sys import argv

if len(argv) == 2:
    name = argv[1]
    cowsay.trex(f"Hello, {name}")
else:
    print("ERROR")
