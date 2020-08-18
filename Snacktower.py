n = int(input())

l = [int(x) for x in input().split()]
found = []
rn = n

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
