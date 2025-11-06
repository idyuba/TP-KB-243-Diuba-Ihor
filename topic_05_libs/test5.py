
from sys import argv

print(argv)

if len(argv) == 3:
    result = int(argv[1]) + int(argv[2])
    print(f"result of adding {argv[1]} and {argv[2]} = {result}")
else:
    print("ERROR: no anought parameters for calculating")
