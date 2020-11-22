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


n, m = map(int, input().split())

l = []

for _ in range(m):
    a, b = map(int, input().split())
    t = (b, a)
    l.append(t)

l.sort(reverse=True)
# print(l)
max_match, i = 0, 0
while i < m and n:
    x = min(n, l[i][1])
    max_match += l[i][0] * x
    n -= x
    i += 1

print(max_match)
