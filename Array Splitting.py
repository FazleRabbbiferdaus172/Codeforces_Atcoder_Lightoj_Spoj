n, k = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]
ll = []
for i in range(n-1):
    ll.append(l[i]-l[i+1])

ans = l[-1] - l[0]

ll.sort()
print(ans, ll)
for i in ll[:k-1]:
    ans += i

print(ans)
