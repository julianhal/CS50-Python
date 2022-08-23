# Solution to https://cs50.harvard.edu/python/2022/psets/3/taqueria/

import sys

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

bank = 0
while True:
    # Take input and check for CTRL-d
    try:
        item = input("Item: ")
    except EOFError:
        print("\n")
        sys.exit()
    # Check if item is in menu and update total cost
    try:
        cost = menu[item.title()]
    except KeyError:
        pass
    else:
        bank += cost
        print(f"Total: ${bank:0.2f}")
