import math


def digi_sum(n):
    ds = 0
    for i in str(n):
        ds += ord(i) - 48
    return ds


for _ in range(int(input())):
    n = int(input())

    while math.gcd(n, digi_sum(n)) == 1:
        n += 1
    print(n)
