n = int(input())
xx = []
yy = []
for _ in range(n):
    x, y = map(int, input().split())
    xx.append(x)
    yy.append(y)

ans = 0
for i in range(n):
    a, b = xx[i], yy[i]

    left, right, up, down = False, False, False, False

    for j in range(n):
        if j == i:
            continue
        if yy[j] == b and xx[j] > a:
            right = True
        if yy[j] == b and xx[j] < a:
            left = True
        if xx[j] == a and yy[j] > b:
            up = True
        if xx[j] == a and yy[j] < b:
            down = True

    if right and left and up and down:
        ans += 1

print(ans)
