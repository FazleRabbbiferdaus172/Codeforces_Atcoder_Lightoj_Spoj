a, b, n = map(int, input().split())

a *= 10
i = 1
while a % b != 0 and i < 10:
    a += 1
    i += 1
if a % b != 0:
    print(-1)
else:
    j = 10 ** (n-1)
    print(a*j)
