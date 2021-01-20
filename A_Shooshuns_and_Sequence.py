n, k = map(int, input().split())

l = list(map(int, input().split()))
a = l[0]
x = 0
for i in range(n):
    if a != l[i]:
        x = i
        a = l[i]
# print(x)
if x <= k-1:
    print(len(l[:x]))
else:
    print(-1)
