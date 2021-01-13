n, m = map(int, input().split())
nn = n
l = list(map(int, input().split()))
ll = l.copy()
mx, mn = 0, 0

while n:
    mn += min(l)
    ind = l.index(min(l))
    l[ind] -= 1
    if l[ind] == 0:
        l[ind] = 1000000
    n -= 1

while nn:
    mx += max(ll)
    ind = ll.index(max(ll))
    ll[ind] -= 1
    nn -= 1

print(mx, mn)
