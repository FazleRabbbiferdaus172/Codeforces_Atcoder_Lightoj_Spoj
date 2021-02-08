n = int(input())
l = list(map(int, input().split()))
ans, c = 1, 1
for i in range(1, n):
    if l[i] < l[i-1]:
        ans = max(c, ans)
        c = 1
    else:
        c += 1


ans = max(c, ans)
print(ans)
