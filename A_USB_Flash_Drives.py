n = int(input())
m = int(input())
d = []
for _ in range(n):
    d.append(int(input().strip()))

d.sort(reverse=True)
ans = 0
c = 0
for i in d:
    ans += i
    if ans >= m:
        c += 1
        break
    c += 1

print(c)
