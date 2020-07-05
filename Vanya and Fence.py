n, h = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]

l.sort()
c = 0
for i in l:
    if i > h:
        break
    c += 1

print(c*1+(len(l)-c)*2)
