# Solution to https://cs50.harvard.edu/python/2022/psets/3/grocery/

import sys

# Specs =  all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
dict = {}
while True:
    # Take input and check for CTRL-d
    try:
        item = input()
    except EOFError:
        print("\n")
        for food in sorted(dict):
            print(f"{dict[food]} {food}")
        sys.exit()
    else:
        try:
            dict.update({item.upper(): dict[item.upper()] + 1})
        except KeyError:
            dict[item.upper()] = 1
