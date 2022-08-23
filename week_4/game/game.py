# Solution to https://cs50.harvard.edu/python/2022/psets/4/game/

import random
import sys

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level >= 1:
            n = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    pass
                else:
                    if guess >= 1:
                        if guess < n:
                            print("Too small!")
                        elif guess > n:
                            print("Too large!")
                        elif guess == n:
                            print("Just right!")
                            sys.exit()
