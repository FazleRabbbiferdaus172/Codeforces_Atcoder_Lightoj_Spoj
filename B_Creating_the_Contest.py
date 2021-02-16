n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    j = i
    while j+1 < n and l[j+1] < l[j]*2:
        j += 1
    ans = max(ans, j-i+1)
    i = j
print(ans)
