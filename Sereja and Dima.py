n = int(input())

l = [int(x) for x in input().split()]
s, d = [], []
while(len(l)):
    if len(l) == 1:
        c = max(l[0], l[-1])
        s.append(c)
        l.pop(l.index(c))
        break
    c = max(l[0], l[-1])
    s.append(c)
    l.pop(l.index(c))
    c = max(l[0], l[-1])
    d.append(c)
    l.pop(l.index(c))

print(sum(s), sum(d))
