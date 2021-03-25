que = []
ans = []
for i in range(3):
    for j in range(5):
        col = j*3 + (i+1)
        row = i * 5 + (j + 1)
        # print("(", i+1, j+1, ")",  end=" ")
        # print("{} {} {}".format(i+1, j+1, col))
        que += ["{} {} {}".format(3, 5, col)]
        ans += [row]
for i in ans:
    print(i)
