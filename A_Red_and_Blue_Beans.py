for _ in range(int(input())):
    r, b, d = map(int, input().split())
    xx, xy = max(r, b) // min(r, b), max(r, b) % min(r, b)
    #print(xx, xy)
    if xx - 1 > d:
        print("NO")
    else:
        if xy == 0:
            print("YES")
        elif xy > 0 and xx <= d:
            print("YES")
        else:
            print("NO")
