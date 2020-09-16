x, y = [int(x) for x in input().split()]

c = 0
for i in range(1, x+1):
    c += (y+(i % 5))//5

print(c)
