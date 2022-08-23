# Solution to https://cs50.harvard.edu/python/2022/psets/1/interpreter/

eqa = input("Expression: ")


l = eqa.split()

if l[1] == "+":
    print(float(int(l[0]) + int(l[2])))
elif l[1] == "-":
    print(float(int(l[0]) - int(l[2])))
elif l[1] == "*":
    print(float(int(l[0]) * int(l[2])))
elif l[1] == "/":
    print(float(int(l[0]) / int(l[2])))
