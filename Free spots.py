
while True:
    w, h, n = map(int, input().split(" "))
    if w == 0 and h == 0 and n == 0:
        break
    total = [[0]*w for i in range(h)]
    xx = 0
    subg = []
    for _ in range(n):
        x = list(map(int, input().split(" ")))
        for i in range(min(x[1], x[3]) - 1, max(x[1], x[3])):
            for j in range(min(x[0], x[2]) - 1, max(x[0], x[2])):
                total[i][j] = 1

    ans = 0
    for i in total:
        ans += i.count(0)
    if ans == 0:
        print("There is no empty spots.")
    elif ans == 1:
        print("There is one empty spot.")
    else:
        print("There are {} empty spots.".format(ans))
    input()
