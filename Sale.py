import sys
input = sys.stdin.readline


def list_input():
    return list(map(int, input().split()))


def float_compare(a, b):
    if abs(a-b) < float(1e-9):
        return True
    else:
        return False


def sub_mod(x, mod):
    x = x % mod
    if x < 0:
        x += mod
    return x


def divisor(n):
    i = 1
    dv = []
    while i*i <= n:
        if n % i == 0:
            dv.append(i)
            if i*i != n:
                dv.append(n//i)
        i += 1

    return dv


#l = list_input()
# print(divisor(25))
# print(divisor(18))
# print(float(1e-9))
n, m = map(int, input().split())

l = sorted(list_input())
earn = 0
i, j = 0, 0

while i < len(l) and m:
    if l[i] < 0:
        earn -= l[i]
        m -= 1
    i += 1
print(earn)
