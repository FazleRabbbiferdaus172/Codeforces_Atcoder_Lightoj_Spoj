import math
for _ in range(int(input())):
    n, d = map(int, input().split())
    i = n//2
    if d <= n:
        print("YES")
    elif math.ceil(d/(i+1)) + i <= n:
        print("YES")
    else:
        print("NO")
