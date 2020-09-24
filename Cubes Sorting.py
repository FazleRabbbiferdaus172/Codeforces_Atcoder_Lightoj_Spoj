for _ in range(int(input())):
    n = int(input())

    l = [int(x) for x in input().split()]
    lr = sorted(l, reverse=True)
    s = set(l)

    if lr == l and len(s) == n:
        print("NO")
    else:
        print("YES")
