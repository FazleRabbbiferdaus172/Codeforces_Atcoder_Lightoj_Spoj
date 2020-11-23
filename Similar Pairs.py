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
    l = list_input()

    p = [i % 2 for i in l]

    if p.count(1) % 2 == 0 and p.count(0) % 2 == 0:
        print("YES")
    else:
        flag = "NO"
        l.sort()
        for i in range(n-1):
            if abs(l[i] - l[i + 1]) == 1:
                flag = "YES"
                break

        print(flag)
