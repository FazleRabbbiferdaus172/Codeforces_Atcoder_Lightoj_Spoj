ans = 7
for i in range(6, -1, -1):
    ans &= i
    print(i, ans)
