for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]

    l.sort()

    s = set(l)
    if len(s) < len(l):
        print("YES")
    else:
        print("NO")
