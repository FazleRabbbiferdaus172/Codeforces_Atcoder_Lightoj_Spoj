n, m, k = list(map(int, input().split()))

l = []


for i in range(m+1):
    l.append(int(input()))

x = l[-1]
l.pop(-1)
ans = 0
for i in l:
    found = i ^ x
    dif = str(bin(found))
    dif = dif.count('1')
    if dif <= k:
        ans += 1

print(ans)
