for _ in range(int(input())):
    n, m = map(int, input().split())

    mat = []

    for i in range(n):
        mat.append(list(map(int, input().split())))

    non_move_x = []
    non_move_y = []
    for x, i in enumerate(mat):
        for y, j in enumerate(i):
            if j == 1:
                non_move_x.append(x)
                non_move_y.append(y)

    zero_count = 0
    for x, i in enumerate(mat):
        for y, j in enumerate(i):
            if x in non_move_x or y in non_move_y:
                continue
            else:
                zero_count += 1
                non_move_x.append(x)
                non_move_y.append(y)

    ans = ["Vivek", "Ashish"]
    print(ans[zero_count % 2])
