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


for _ in range(int(input())):
    n = int(input().strip())
    if n % 2 == 0:
        for i in range(n, 0, -1):
            print(i, end=" ")
        print()
    else:
        print(n//2+1, end=" ")
        for i in range(n, 0, -1):
            if i == abs(n)//2 + 1:
                continue
            print(i, end=" ")
        print()
