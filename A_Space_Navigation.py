for _ in range(int(input())):
    x, y = map(int, input().split())
    s = input()
    d = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
    for i in s:
        d[i] += 1
    xok = False
    yok = False
    if x >= 0 and d['R'] >= x:
        xok = True
    elif x < 0 and d['L'] >= abs(x):
        xok = True

    if y >= 0 and d['U'] >= y:
        yok = True
    elif y < 0 and d['D'] >= abs(y):
        yok = True

    if xok and yok:
        print("YES")
    else:
        print("NO")
