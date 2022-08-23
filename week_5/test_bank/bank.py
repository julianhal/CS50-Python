# Solution to https://cs50.harvard.edu/python/2022/psets/1/bank/


def main():
    greeting = input("Greeting: ")

    result = value(greeting)
    print(f"${result}")


def value(greeting):
    x = greeting.lower().strip()
    if x.startswith("hello"):
        return 0
    elif x.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
