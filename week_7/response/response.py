# Solution to https://cs50.harvard.edu/python/2022/psets/7/response/

from validators import email

s = input("Email: ")

if email(s):
    print("Valid")
else:
    print("Invalid")
