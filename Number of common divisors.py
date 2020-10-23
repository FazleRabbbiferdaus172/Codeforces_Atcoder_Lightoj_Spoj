import math
factor = [[] for i in range(10**6+1)]

for i in range(1, 10**6+1):
    for j in range(i, 10**6+1, i):
        factor[j].append(i)

for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    j = math.gcd(a, b)
    print(len(factor[j]))
