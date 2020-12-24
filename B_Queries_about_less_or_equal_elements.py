n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
z = int(1e9)+7
a = [-1*z] + a + [z]
b = list(map(int, input().split()))
ans = []
for i in b:
    l, r = 1, n+1
    while l < r:
        mid = (l+r)//2
        #print(mid, a[mid])
        if a[mid] <= i:
            l = mid+1
        else:
            r = mid
    #print("query end")
    ans.append(l-1)

print(*ans)
