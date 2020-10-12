import math

n, k = [int(x) for x in input().split()]

if n < k:
    print('NO')
elif (n & (n-1)) == 1 and k == 1:
    print('NO')
elif k < list(bin(n)).count('1'):
    print('NO')
else:
    print('YES')
    l = [1]*k
    i = 0
    n -= k
    while n > 0 and i < k:
        while l[i] <= n:
            n -= l[i]
            l[i] *= 2
        i += 1
    print(*l)
