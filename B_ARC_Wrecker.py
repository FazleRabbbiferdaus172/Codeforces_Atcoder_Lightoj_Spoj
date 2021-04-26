n = int(input())
mod = int(1e9) + 7
l = sorted([0] + list(map(int, input().split())))
ans = 1
for i in range(1, n+1):
    ans *= (l[i] - l[i-1] + 1)
    ans %= mod
print(ans % mod)
