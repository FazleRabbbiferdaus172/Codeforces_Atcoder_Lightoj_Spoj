n = int(input())

l = [int(x) for x in input().split()]
l.sort(reverse=True)
lst = l[0] + 2
ans = 0
for o, i in enumerate(l):
    cur = -1
    for dx in range(1, -2, -1):
        if i + dx > 0 and i + dx < lst:
            cur = i + dx
            break
    if cur == -1:
        continue
    ans += 1
    lst = cur
    #print(i, d)
# print(d)
print(ans)
