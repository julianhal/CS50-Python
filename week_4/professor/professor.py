# Solution to https://cs50.harvard.edu/python/2022/psets/4/professor/

import random
import sys


def main():
    level = get_level()
    score = 0
    problems = []
    # Survery the user 10 times with 10 distinct problems
    for _ in range(10):
        print(_)
        # Generate distinct equation
        while True:
            x = generate_integer(level)
            y = generate_integer(level)
            if (x, y) in problems or (y, x) in problems:
                pass
            else:
                problems.append((x, y))
                problems.append((y, x))
                break

        ans = x + y
        tries = 0

        # Guess equations
        while True:
            if tries == 3:
                print(f"{x} + {y} = {ans}")
                break
            else:
                try:
                    print(f"{x} + {y} = ", end="")
                    guess = int(input())
                    if guess == ans:
                        tries = 0
                        score += 1
                        break
                    else:
                        raise ValueError
                except ValueError:
                    tries += 1
                    print("EEE")
                    continue

    # Print score
    print(f"Score: {score}")
    sys.exit()


# Take input of level 1, 2 or 3
def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            n = int(input("Level: "))
            if n not in levels:
                raise ValueError
        except ValueError:
            pass
        else:
            return n


# Produce random numbers for the equations depending on level
def generate_integer(level):
    if level == 1:
        return random.randint(0, 10)
    elif level == 2:
        return random.randint(10, 100)
    else:
        return random.randint(100, 1000)


if __name__ == "__main__":
    main()
