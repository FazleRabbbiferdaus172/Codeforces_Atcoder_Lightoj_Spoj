for _ in range(int(input())):
    l = list(input())

    s = "".join(sorted(l))
    #ss = "".join(l)

    if l.count(l[0]) == len(l):
        print(-1)
    else:
        print(s)
