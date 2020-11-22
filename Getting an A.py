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


def rnd(a, b):
    x = a/b
    y = a//b
    if x - y >= .5:
        return y+1
    else:
        return y


n = int(input())
l = list_input()
m_ans = 0
while rnd(sum(l), n) != 5:
    l[l.index(min(l))] = 5
    m_ans += 1
    #print(l, sum(l), rnd(sum(l), n), sum(l)/n)

print(m_ans)
