import math


def factors(x, k):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x//i != i:
                result.append(x//i)
                if (x//i) % k != 0:
                    return x//i
            elif x//i == i:
                if (x//i) % k != 0:
                    return x//i
        i += 1


for _ in range(int(input())):
    p, q = [int(x) for x in input().split()]

    fac = factors(p, q)

    print(fac)
