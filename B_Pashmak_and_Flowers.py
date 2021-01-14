n = int(input())
l = list(map(int, input().split()))

l.sort()
ans1 = l[-1] - l[0]
a = l.count(l[0])
b = l.count(l[-1])
ans2 = a*b
if ans1 == 0:
    ans2 = 0
    for i in range(n-1):
        ans2 += n - (i+1)
print(ans1, ans2)
