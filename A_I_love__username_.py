n = int(input())
l = list(map(int, input().split()))

mx, mn = l[0], l[0]
c = 0
for i in l[1:]:
    if i > mx:
        mx = i
        c += 1
    elif i < mn:
        mn = i
        c += 1

print(c)
