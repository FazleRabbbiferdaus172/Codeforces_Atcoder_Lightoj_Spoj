n, m = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
frq = dict()
for i in range(1, m+1):
    frq[i] = b.count(i)
b.sort(reverse=True)
x = -1
past = 0
for j, i in enumerate(b):
    if i != x:
        past = len(b[j:]) - frq[i]
        x = i
        ans += past
        #print(n - frq[i])
    elif i == x:
        ans += past
    # print(past)
print(ans)
