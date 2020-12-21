n, l = map(int, input().split())

li = list(map(int, input().split()))

li.sort()

mx = 0
for i in range(n-1):
    mx = max(mx, li[i+1]-li[i])
fcor = li[0]
lcor = (l - li[-1])
#print("fcor", fcor, "lcor", lcor)
ans = max(fcor, lcor, mx/2)

print(ans)
