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

n = int(input().strip())
s = input().strip()
x, y = 0, 0
pay = 0
for j, i in enumerate(s):
    if i == 'R':
        x += 1
    else:
        y += 1
    if x == y and j < n-1 and s[j] == s[j+1]:
        pay += 1
print(pay)
