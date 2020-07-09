d = {}
n = [int(x) for x in input().split()]
for i, j in enumerate(n, 1):
    d[i] = j

s = list(input())
t = 0
for i in s:
    t += d[int(i)]

print(t)
