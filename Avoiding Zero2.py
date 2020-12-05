for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if sum(l) == 0:
        print("NO")
    else:
        print("YES")
        if sum(l) > 0:
            l.sort(reverse=True)
        else:
            l.sort()

        print(*l)
