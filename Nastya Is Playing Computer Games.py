n, k = map(int, input().split())

if k == 1 or k == n:
    print(n*3)
else:
    print(n*3 + min(k-1, n-k))
