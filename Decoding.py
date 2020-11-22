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
d = list(input().strip())

s = [-1]*n
#ini = n//2
if n % 2 == 1:
    #ini = n//2 - 1
    ini = n//2
    s[ini] = d[0]
    even, odd = 1, 1
    for i in range(1, n):
        if i % 2 == 1:
            s[ini-odd] = d[i]
            odd += 1
        else:
            s[ini+even] = d[i]
            even += 1

else:
    ini = n//2 - 1
    #ini = n//2
    s[ini] = d[0]
    even, odd = 1, 1
    for i in range(1, n):
        if i % 2 == 1:
            s[ini+odd] = d[i]
            odd += 1
        else:
            s[ini-even] = d[i]
            even += 1


# print(s)
print("".join(s))
