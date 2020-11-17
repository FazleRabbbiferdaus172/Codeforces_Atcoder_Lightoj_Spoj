import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    if max(l) - k > min(l) + k:
        print(-1)
    else:
        print(min(l)+k)
