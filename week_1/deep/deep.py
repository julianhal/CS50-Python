# Solution to https://cs50.harvard.edu/python/2022/psets/1/deep/

q = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)

l = {"42", "forty-two", "forty two"}

if q.lower().strip() in l:
    print("Yes")
else:
    print("No")
