n, m = map(int, input().split())

l = [-1] + list(map(int, input().split()))
ansm = 0
ans = n
for i in range(1, n+1):

    if l[i] <= m:
        l[i] = 0
    else:
        if l[i] % m == 0:
            l[i] = l[i]//m
        else:
            l[i] = l[i]//m + 1
        if l[i] >= ansm:
            ans = i
            ansm = l[i]

print(ans)
