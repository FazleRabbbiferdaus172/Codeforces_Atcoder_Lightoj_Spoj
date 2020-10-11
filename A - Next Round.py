n, k = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]
if a.count(0) == n:
    print(0)
else:
    k = k - 1
    i = 0
    while i < n and a[i] >= a[k] and a[i] != 0:
        i += 1
    print(i)
