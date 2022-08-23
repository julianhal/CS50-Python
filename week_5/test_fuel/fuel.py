import sys
import sys


def main():
    frac = get_input("Fraction: ")

    x = round(frac * 100)
    if x <= 1:
        sys.exit("E")
    if x >= 99:
        sys.exit("F")
    print(f"{x}%")


def get_input(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            div = int(x) / int(y)
        except (ValueError, ZeroDivisionError):
            print("Invalid input!")
        else:
            if div <= 1:
                return div
        print("x greater than y!")


if __name__ == "__main__":
    main()
