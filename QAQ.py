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


s = input().strip()

l = list(s)

for i in range(len(l)):
    if l[i] != 'Q' and l[i] != 'A':
        l[i] = '$'

while '$' in l:
    l.remove('$')

while len(l) != 0 and l[0] == 'A':
    l.pop(0)
while len(l) != 0 and l[-1] == 'A':
    l.pop(-1)

count = 0
# print(l)
for i in range(len(l)):
    if l[i] == 'A':
        q1, q2 = l[0:i].count('Q'), l[i:].count('Q')
        count += q1*q2

print(count)
