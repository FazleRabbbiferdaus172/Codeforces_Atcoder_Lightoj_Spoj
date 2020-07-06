n = int(input())

l = [[int(x) for x in input().split()] for i in range(n)]

c = 0

for i in l:
    if i.count(1) >= 2:
        c += 1


print(c)
