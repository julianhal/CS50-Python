# Solution to https://cs50.harvard.edu/python/2022/psets/1/extensions/#file-extensions

import mimetypes

name = input("File name: ")

mt = mimetypes.guess_type(name.strip().lower())
if mt[0] == None:
    print("application/octet-stream")
else:
    print(mt[0])
