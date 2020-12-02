l = int(input())
i = 1
s = set(list(str(l+i)))

while len(s) != 4:
    i += 1
    s = set(list(str(l+i)))
print(l+i)
