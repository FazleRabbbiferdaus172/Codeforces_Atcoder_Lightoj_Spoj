import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    count = 0
    ans = []
    for i in range(n, 0, -1):
        if k % 2 == 0 and i >= math.ceil(k//2) and i != k:
            ans += [i]
            count += 1
        elif k % 2 == 1 and i > math.ceil(k//2) and i != k:
            ans += [i]
            count += 1
    print(count)
    print(*ans)
