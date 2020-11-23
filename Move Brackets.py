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
    n = map(int, input())

    s = list(input().strip())
    # print(s)
    open_b = []

    for i in s:
        if i == '(':
            open_b.append('(')
        elif i == ')' and len(open_b) != 0:
            open_b.pop(-1)

    print(len(open_b))
    # print(close_b)
