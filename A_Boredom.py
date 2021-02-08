n = int(input())
l = sorted(list(map(int, input().split())))
cnt = [0] + [0]*int(1e5)

for i in l[:n+1]:
    cnt[i] += 1

dp = [0] + [0]*int(1e5)
dp[1] = cnt[1]


for i in range(2, int(1e5)+1):
    dp[i] = max(dp[i-1], dp[i-2]+cnt[i]*i)

print(dp[-1])
