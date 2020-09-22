n, k = [int(x) for x in input().split()]

s = 0
for _ in range(n):
    r, l = [int(x) for x in input().split()]
    s += (l-r) + 1

print((k-(s % k)) % k)
