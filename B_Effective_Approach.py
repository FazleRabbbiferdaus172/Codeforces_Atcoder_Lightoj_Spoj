n = int(input())

l = [0] + list(map(int, input().split()))

d = {}

for i, j in enumerate(l):
    d[j] = i

q = int(input())
qq = list(map(int, input().split()))
ansv, ansp = 0, 0
for i in qq:
    v, p = d[i], n - d[i] + 1
    ansv += v
    ansp += p
print(ansv, ansp)
