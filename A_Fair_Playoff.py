for _ in range(int(input())):
    l = list(map(int, input().split()))
    x = sorted(l, reverse=True)
    # print(x)
    # print(l)
    mx1, mx2 = x[0], x[1]
    gp1, gp2 = l[:2], l[2:]
    #print(mx1, mx2)
    #print(gp1, gp2)
    if mx1 in gp1 and mx2 in gp1:
        print("NO")
    elif mx1 in gp2 and mx2 in gp2:
        print("NO")
    else:
        print("YES")
