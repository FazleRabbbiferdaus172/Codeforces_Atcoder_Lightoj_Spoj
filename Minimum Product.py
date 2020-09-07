t = int(input())

for _ in range(t):
    a, b, x, y, n = [int(x) for x in input().split()]
    j = min(n, a-x)
    k = min(n, b-y)
    if a - j < b - k:
        print((a-j)*(b-min((n-j), k)))
    else:
        print((b-k)*(a-min((n-k), j)))
