x, y = [int(x) for x in input().split()]
d = 0
for i in range(x):
    a, b = input().split()
    if a == '+':
        y += int(b)
    else:
        if int(b) <= y:
            y -= int(b)
        else:
            d += 1
print(y, d)
