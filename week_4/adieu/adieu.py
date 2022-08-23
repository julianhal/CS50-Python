# Solution to https://cs50.harvard.edu/python/2022/psets/4/adieu/

import inflect
import sys

p = inflect.engine()

# Prompt user for names and quit when CTRL-d is inputed
tmp = []
names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        # Print names one at a time
        print("\n")
        for i in range(len(names)):
            print(f"Adieu, adieu, to {names[i]}")
        sys.exit()
    else:
        tmp.append(name)
        names.append(p.join(tmp))
