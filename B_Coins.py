d = {'A': '', 'B': '', 'C': ''}
l = []
l += [input()]
l += [input()]
l += [input()]

# print(d)
for i in l:
    x = list(i)
    if x[1] == '>':
        d[x[0]] += x[2]
    else:
        d[x[2]] += x[0]
for i in d:
    d[i] = len(d[i])

if 2 in d.values():
    # print(d)
    d = sorted(d, key=d.get)
    print("".join(d))
else:
    print("Impossible")
