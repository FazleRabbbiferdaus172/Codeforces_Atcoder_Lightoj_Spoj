import numpy as np


def solve(i, mask):
    global n, a, dp
    if mask == (1 << n) - 1:
        return 0

    if dp[i][mask] != -1:
        return dp[i][mask]
    for j in range(n):
        if (mask & (1 << j)) == 0:
            dp[i][mask] = max(dp[i][mask], a[i][j]+solve(i+1, mask | (1 << j)))
    return dp[i][mask]


for test in range(int(input())):
    n = int(input())
    a = [[0]*16 for i in range(16)]
    dp = [[-1]*(1 << 16) for i in range(16)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    ans = solve(0, 0)
    print("Case {}: {}".format(test+1, ans))
