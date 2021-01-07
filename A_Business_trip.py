k = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
c = 0
d = 0
for i in l:
    if d < k:
        d += i
        c += 1
    else:
        break
else:
    if d == k:
        c = 12
    else:
        c = -1

print(c)
