n = int(input())
l = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i+1, n+1):
        m = l.count(1) + l[i:j].count(0) - l[i:j].count(1)
        ans = max(ans, m)
print(ans)
