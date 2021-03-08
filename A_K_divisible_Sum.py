import math
for _ in range(int(input())):
    n, k = map(int, input().split())

    if n > k:
        x = math.ceil(n / k)
        k *= x
    print(math.ceil(k/n))
