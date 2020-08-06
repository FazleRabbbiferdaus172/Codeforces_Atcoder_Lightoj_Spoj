t = int(input())

for ti in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    xa = min(a)
    xb = min(b)
    c = 0
    for i in range(n):
        if a[i] > xa and b[i] > xb:
            c += max(a[i]-xa, b[i]-xb)
        else:
            c += a[i] - xa
            c += b[i] - xb
    print(c)
