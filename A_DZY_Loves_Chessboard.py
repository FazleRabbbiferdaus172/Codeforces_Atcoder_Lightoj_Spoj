n, m = map(int, input().split())
s = ['B', 'W']
for i in range(n):
    for k, j in enumerate(input()):
        if j == ".":
            if i % 2 == 0:
                print(s[k % 2], end="")
            else:
                print(s[(k+1) % 2], end="")

        else:
            print("-", end="")
    print("")
