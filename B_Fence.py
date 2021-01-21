n, k = map(int, input().split())
l = [0]+list(map(int, input().split()))
# print(l)
j = sum(l[:k])
mn = float('inf')
ans = 1
for i in range(1, n-k+2):
    j = j - l[i-1] + l[i+k-1]
    # print(j)
    if j < mn:
        mn = j
        ans = i

print(ans)
