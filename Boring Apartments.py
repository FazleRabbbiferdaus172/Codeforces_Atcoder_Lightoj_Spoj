for _ in range(int(input())):
    n = int(input())
    s, si, c = "1", 1, 0
    x = 0
    while int(s) != n:
        c += len(s)
        s += str(si)
        # print(s)
        if len(s) > 4:
            si += 1
            #print("j", si)
            s = str(si)
            #print("ifs", s)

    print(c+len(s))
