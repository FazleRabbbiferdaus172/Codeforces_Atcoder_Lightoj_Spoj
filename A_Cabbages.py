n, a, x, y = map(int, input().split())
if n > a:
    ans = (n-a)*y + a*x
else:
    ans = n*x
print(ans)
