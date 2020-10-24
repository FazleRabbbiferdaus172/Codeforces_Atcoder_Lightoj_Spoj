for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    s = sum(l)
    if s == m:
        print("YES")
    else:
        print("NO")
