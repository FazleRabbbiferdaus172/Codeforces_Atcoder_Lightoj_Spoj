import math


def lcm(*n):
    ans = 1
    for i in n:
        ans *= (i//gcd(i, ans))
    return ans


def gcd(*n):
    ans = 0
    for i in n:
        ans = math.gcd(ans, i)
    return ans


print(gcd(*[10, 50, 30, 25, 13]))
print(lcm(10, 50, 25, 7))
