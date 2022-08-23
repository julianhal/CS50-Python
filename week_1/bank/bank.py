# Solution to https://cs50.harvard.edu/python/2022/psets/1/bank/

greeting = input("Greeting: ")

x = greeting.lower().strip()
if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")
