n = int(input())
l = [int(x) for x in input().split()]
c = [0]*n
before, after, x = 0, 1, 0
while after < n and l[x] >= l[after]:
    c[0] += 1
    after += 1
    x += 1

for i in range(1, n-1):
    x = i
    before = i - 1
    after = i + 1
    while before >= 0 and l[x] >= l[before]:
        c[i] += 1
        before -= 1
        x -= 1
    x = i
    after = i + 1
    while after < n and l[x] >= l[after]:
        c[i] += 1
        after += 1
        x += 1

x = n-1
before = n-2
while before >= 0 and l[x] >= l[before]:
    c[n-1] += 1
    before -= 1
    x -= 1

print(max(c)+1)
