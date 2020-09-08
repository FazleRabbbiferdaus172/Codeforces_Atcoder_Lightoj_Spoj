n = int(input())

l = [int(x) for x in input().split()]
found = [False]*(n+1)
rn = n
'''
for i in l:
    if i == rn:
        found.insert(0, i)
        while len(found) != 0 and rn in found:
            x = found.pop(found.index(rn))
            print(x, end=" ")
            rn -= 1
        print("")

    else:
        print("")
        found.insert(0, i)
'''
c = n

for i in l:
    found[i] = True

    while found[c] and c > 0:
        print(c, end=" ")
        c -= 1
    print()
