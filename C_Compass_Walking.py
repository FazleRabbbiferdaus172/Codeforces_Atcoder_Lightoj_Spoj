import math
r, x, y = map(int, input().split())

ans = (x**2 + y ** 2)**.5

if ans < r:
    ans = math.ceil(ans/r) + 1
else:
    ans = math.ceil(ans/r)

print(ans)
