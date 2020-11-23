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


n = int(input().strip())
l = list_input()
d = dict()
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

xx = max(list(d.values()))
if xx > 2:
    print("NO")
else:
    print("YES")
    inc, dec = [], []
    for i in d.keys():
        if d[i] == 1:
            inc.append(i)
            d[i] -= 1
        else:
            inc.append(i)
            dec.append(i)
            d[i] -= 2

    inc.sort()
    dec.sort(reverse=True)
    print(len(inc))
    print(*inc)
    print(len(dec))
    print(*dec)
