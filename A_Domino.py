import sys
n = int(input())
upper, lower = [], []
for _ in range(n):
    x, y = map(int, input().split())
    upper += [x % 2]
    lower += [y % 2]
c = 0
if upper.count(1) == n and lower.count(1) == n and n % 2 == 1:
    print(-1)
    sys.exit(0)
while sum(upper) % 2 == 1 and sum(lower) % 2 == 1:
    non = 0
    for i in range(n):
        if (upper[i] == 1 and lower[i] == 0) or (upper[i] == 0 and lower[i] == 1):
            upper[i], lower[i] = lower[i], upper[i]
        else:
            non += 1
        if sum(upper) % 2 == 0 and sum(lower) % 2 == 0:
            break
    if non == n:
        break

    c += 1
if c == 0 and (sum(upper) % 2 == 1 or sum(lower) % 2 == 1):
    c = -1
print(c)
