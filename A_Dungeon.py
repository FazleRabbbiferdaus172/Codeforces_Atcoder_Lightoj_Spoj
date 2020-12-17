for _ in range(int(input())):

    x = list(map(int, input().split()))

    m = min(x)

    s = sum(x)

    xx = s % 9
    fxx = s // 9
    #print(xx, fxx)
    if xx == 0 and m >= fxx:
        print("YES")
    else:
        print("NO")
