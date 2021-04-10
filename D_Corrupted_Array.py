for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    x1, x2 = l[-1], l[-2]
    s1 = sum(l) - x1
    s2 = sum(l) - x2
    for i in range(n+2):
        s1 -= l[i]
        s2 -= l[-1]
        if s1 == x1:
            # print("yes")
            l.pop(i)
            l.remove(x1)
            break
        elif s2 == x2:
            # print("yes")
            l.pop(i)
            l.remove(x2)
            break
        s1 += l[i]
        s2 += l[i]
    else:
        print(-1)
        continue
    print(*l)
