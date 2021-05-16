import math
for _ in range(int(input())):
    ep = int(input())
    wp = 100 - ep
    g = math.gcd(ep, wp)
    print(ep//g + wp//g)
