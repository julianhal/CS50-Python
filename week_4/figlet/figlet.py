# Solution to https://cs50.harvard.edu/python/2022/psets/4/figlet/

from sys import argv, exit
from pyfiglet import Figlet
from random import choice

figlet = Figlet()

# Random figlet font
if len(argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=choice(figlet.getFonts()))
    print(figlet.renderText(text))

# Custom figlet font
if (
    len(argv) == 3
    and (argv[1] == "-f" or argv[1] == "--font")
    and argv[2] in figlet.getFonts()
):
    text = input("Input: ")
    figlet.setFont(font=argv[2])
    print(figlet.renderText(text))
else:
    exit("Usage: './figlet.py -f font'")
