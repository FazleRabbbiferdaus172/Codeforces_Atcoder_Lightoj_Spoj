import math
for _ in range(int(input())):
    a, b = map(int, input().split())
    z = a*b + a
    x = a*b
    y = a
    if b == 1:
        print("NO")
    else:
        print("YES")
        print(x, y, z)
