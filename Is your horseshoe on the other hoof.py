l = [int(x) for x in input().split()]
s = set(l)
c = 0
for i in s:
    c += l.count(i)-1

print(c)
