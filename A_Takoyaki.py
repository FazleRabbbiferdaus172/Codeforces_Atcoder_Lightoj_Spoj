n, x, t = map(int, input().split())

ans = 0
minit = 0
while ans < n:
    ans += x
    minit += t
print(minit)
