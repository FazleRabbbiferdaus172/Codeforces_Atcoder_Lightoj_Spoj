mod = int(2**30)
a, b, c = map(int, input().split())


def numd(x):
    c = 0
    q = 1
    while q*q <= x:
        if x % q == 0:
            if q != x//q:
                c += 2
            else:
                c += 1
        q += 1
    return c


l = [-1]*((a*b*c)+1)
ans = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            x = i*j*k
            if l[x] == -1:
                l[x] = numd(x)
            ans += l[x]

print(ans)
