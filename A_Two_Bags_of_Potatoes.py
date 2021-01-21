y, k, n = map(int, input().split())
p = False
for i in range(k, n+1, k):
    if i > y:
        print(i-y, end=" ")
        p = True
if p == False:
    print(-1)
else:
    print()
