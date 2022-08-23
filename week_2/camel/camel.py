# Solution to https://cs50.harvard.edu/python/2022/psets/2/camel/
# Learning material: https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3

cc = input("camelCase: ")

for i in cc:
    if not i.islower():
        index = cc.find(i)
        cc = cc[:index] + "_" + cc[index].lower() + cc[index + 1 :]
print(f"snake_case: {cc}")


"""
Alternativ måte å endre en karakter i strengen:
temp = list(cc)
temp[cc.find(i)] = '_' + i.lower()
str = "".join(temp)
"""
