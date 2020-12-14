n = int(input())

x = list(map(int, input().split()))
aa = x[0]
x = x + [aa]
m = int(1e5)
for i in range(1, n+1):
    f = abs(x[i] - x[i-1])
    #print(f, x[i])
    if f < m:
        ans, ans2 = i-1, i % n
        m = f

print(ans+1, ans2+1)
