for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    i = 0
    while l[i] != 1:
        l.pop(i)

    i = -1
    while l[i] != 1:
        l.pop(i)

    j = l.count(0)

    print(j)
