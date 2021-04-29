for _ in range(int(input())):
    fx, fy, m = map(int, input().split())
    if fx*fy - 1 == m:
        print("YES")
    else:
        print("NO")
