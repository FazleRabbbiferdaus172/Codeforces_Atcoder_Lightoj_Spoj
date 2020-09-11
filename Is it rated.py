n = int(input())

l = []

for _ in range(n):
    l.append([int(x) for x in input().split()])

c = 0
for i in l:
    a = set(i)
    if len(a) == 1:
        c += 1

if c != n:
    print("rated")
else:
    d = True
    for i in range(1, n):
        if l[i-1][0] < l[i][0]:
            d = False
    if d == True:
        print("maybe")
    else:
        print("unrated")
