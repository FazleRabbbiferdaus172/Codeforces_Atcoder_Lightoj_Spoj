n, b = map(int, input().split())
a = list(map(int, input().split()))
e, o = 0, 0
lst = 0
temp = []
for i in a:
    if o == e:
        temp += [abs(i - lst)]
        o, e = 0, 0
    if i % 2 == 0:
        o += 1
    else:
        e += 1
    lst = i
c = 0

for i in sorted(temp[1:]):
    b -= i
    if b >= 0:
        c += 1
print(c)
