T = int(input())

for t in range(T):
    x, o = 0, 0
    for _ in range(4):
        xx = input().strip()
        print(xx)
        x += xx.count('x')
        o += xx.count('o')
    if x - o > 1:
        print("no")
    else:
        print("yes")
