n, m, t = map(int, input().split())
mn = n
ans = "Yes"
xx = 0
for _ in range(m):
    a, b = map(int, input().split())

    n -= a - xx
    # print(n)
    if n <= 0:
        ans = "No"
    n += b - a
    if n >= mn:
        n = mn
    # print(n)
    xx = b
#print(n - (t - xx))
if n > mn:
    n = mn
if n - (t - xx) <= 0:
    ans = "No"


print(ans)
