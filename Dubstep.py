n = input()

if "WUB" in n:
    n = n.replace("WUB", " ")
n = n.split()
print(' '.join(n))
