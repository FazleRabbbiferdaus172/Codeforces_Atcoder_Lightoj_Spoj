n, k = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]

m = [l[x] for x in range(1, 2*n+1, 2)]

for i in range(len(m)):
    if k == 0:
        break
    if l[i*2+1-1] != m[i] - 1 and l[i*2+1+1] != m[i] - 1:
        m[i] -= 1
        k -= 1
j = 0
for i in range(1, 2*n+1, 2):
    l[i] = m[j]
    j += 1

print(*l)
