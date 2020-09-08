n = int(input())

l = [int(x) for x in input().split()]
found = [False]*(n+1)
c = n

for i in l:
    found[i] = True

    while found[c] and c > 0:
        print(c, end=" ")
        c -= 1
    print()
