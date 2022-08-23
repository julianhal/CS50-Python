# Solution to https://cs50.harvard.edu/python/2022/psets/6/pizza/

import sys, csv
from tabulate import tabulate

# Validate correct number of comman-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments!")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments!")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file!")


# Load in file into list, then print tabulated list of lists (rows)
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        print(tabulate(rows, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("Not a CSV file!")
