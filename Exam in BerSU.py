n, t = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]
anss = []
for i in range(1, n+1):
    x = sorted(l[:i-1], reverse=True)
    o = l[i-1]
    #print("x, o ", x, o)

    ans = 0
    while sum(x) + o > t and len(x) > 0:
        #print(sum(x), max(x))
        x.remove(max(x))
        ans += 1
    # print(ans)
    anss.append(ans)


print(*anss)
