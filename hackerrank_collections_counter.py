from collections import Counter
x = int(input())
l = Counter(list(map(int, input().split())))
n = int(input())
ans = 0
for _ in range(n):
    s_size, price = map(int, input().split())
    if l[s_size] > 0:
        ans += price
        l[s_size] -= 1
print(ans)
