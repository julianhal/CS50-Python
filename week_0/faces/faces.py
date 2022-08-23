# https://cs50.harvard.edu/python/2022/psets/0/faces/


def main():
    inp = input()
    print(convert(inp), end="")


def convert(x):
    return x.replace(":(", "🙁").replace(":)", "🙂")


if __name__ == "__main__":
    main()
