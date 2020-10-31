import math


def sieve(n):
    mark = [0]*(n+1)
    prime = []
    for i in range(3, n+1, 2):
        if not mark[i]:
            for j in range(3*i, n+1, i+i):
                mark[j] = 1
    prime.append(2)
    for i in range(3, n+1, 2):
        if not mark[i]:
            prime.append(i)

    return prime


def ispowerof2(x):
    if x and not (x & (x-1)):
        return 0
    else:
        return 1


n = int(input())
h = n
prime = sieve(n)
l = []

countp = 0

ans = 1
for i in prime:
    countp = 0
    if n % i == 0:
        ans *= i
        while n % i == 0:
            n //= i
            countp += 1
        l.append(countp)

    if n == 1:
        break
if h > 1:
    maxp = max(l)
else:
    maxp = 0
flag = 0
for i in l:
    if i != maxp:
        flag = 1

temp = 0

if flag:
    temp = 1
else:
    temp = ispowerof2(maxp)

if maxp == 1:
    maxp -= 1
elif maxp != 0:
    maxp = math.ceil(math.log2(maxp)) + temp

print(ans, maxp)
