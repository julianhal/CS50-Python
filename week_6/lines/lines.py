# Solution to https://cs50.harvard.edu/python/2022/psets/6/lines/

import sys

# Check for correct command line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

# Try to open file and count lines in file
try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit(f"File does not exist")
else:
    count = 0
    for line in lines:
        tmp = line.strip()
        if tmp != "" and not tmp.startswith("#"):
            count += 1
    print(count)
    sys.exit()
