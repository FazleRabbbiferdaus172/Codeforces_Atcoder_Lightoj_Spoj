n, m, d = map(int, input().split())
l = []
for _ in range(n):
    l += list(map(int, input().split()))

l.sort()
mid = (n*m)//2
ans = 0
for i in l:
    if abs(i-l[mid]) % d != 0:
        print(-1)
        break
    ans += abs(i - l[mid])
else:
    print(ans//d)
