from collections import defaultdict
n, m = map(int, input().split())
a, b = defaultdict(list), defaultdict(list)
for i in range(1, n+1):
    temp = input()
    a[temp].append(i)
for _ in range(m):
    temp = input()
    if temp in a:
        print(*a[temp])
    else:
        print(-1)
# print(a)
