from typing import Collection


from collections import defaultdict
while True:
    inp = list(map(int, input().split()))
    if len(inp) == 1 and inp.count(0) == 1:
        break
    n, a, b = inp[0], inp[1], inp[2]
    x = 0
    rem = n
    count = defaultdict(int)
    while True:
        x = ((a * (x**2 % n)) % n + b) % n
        count[x] += 1
        if count[x] == 2:
            rem -= 1
        if count[x] == 3:
            break
    print(rem)
    # print("OK")
