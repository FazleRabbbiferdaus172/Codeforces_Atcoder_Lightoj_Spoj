n = int(input())
l = list(map(int, input().split()))
m = dict()

for j, i in enumerate(l):
    m[i] = j+1

ans = 0
x = m[1]
for i in range(2, n+1):
    ans += abs(m[i]-x)
    x = m[i]

print(ans)
