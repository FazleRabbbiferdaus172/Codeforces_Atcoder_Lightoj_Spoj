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

a = input().strip()
b = input().strip()
flag = True
for i in range(len(a)):
    if a[i] < b[i]:
        flag = False
        break

if flag:
    print(b)
else:
    print(-1)
