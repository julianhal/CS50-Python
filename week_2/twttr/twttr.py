# Solution to https://cs50.harvard.edu/python/2022/psets/2/twttr/


def main():
    message = input("Input: ")
    x = shorten(message)

    print(f"Output: {x}")


def shorten(msg):
    vowels = "aeiou"
    for ch in msg:
        if ch.lower() in vowels:
            msg = msg[: msg.find(ch)] + msg[msg.find(ch) + 1 :]
    return msg


if __name__ == "__main__":
    main()
