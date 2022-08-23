# Solution to https://cs50.harvard.edu/python/2022/psets/2/coke/

valid_coins = [25, 10, 5]
cost = 50
while True:
    # Get correct user input
    value = int(input("Insert coin: "))

    if value in valid_coins:
        cost -= value

    # Check if amout due or change owed
    if cost < 0 or cost == 0:
        print(f"Change owed: {abs(cost)}")
        quit()
    else:
        print(f"Amount due: {cost}")
