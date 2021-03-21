for _ in range(int(input())):
    r, c = map(int, input().split())
    g = []
    for _ in range(r):
        g.append(list(map(int, input().split())))

    # print(g)
    count = 0
    for i in range(r):
        rc = 0
        for j in range(c):
            if g[i][j] == 1:
                rc += 1
            else:
                rc = 0
            if rc > 2:
                #print('one seg found', i)
                cc = 0
                for x in range(i, r):
                    if g[x][j] == 1:
                        cc += 1
                    else:
                        break
                    #print(rc, cc)
                    if cc == 2*rc or rc == 2*cc:
                        count += 1

                cc = 0
                for x in range(r-1, -1, -1):
                    if g[x][j] == 1:
                        cc += 1
                    else:
                        break
                    #print(rc, cc)
                    if cc == 2*rc or rc == 2*cc:
                        count += 1
    print("1th", count)
    for i in range(r):
        rc = 0
        for j in range(c-1, -1, -1):
            if g[i][j] == 1:
                rc += 1
            else:
                rc = 0
            if rc > 2:
                #print('one seg found', i)
                cc = 0
                for x in range(i, r):
                    if g[x][j] == 1:
                        cc += 1
                    else:
                        break
                    #print(rc, cc)
                    if cc == 2*rc or rc == 2*cc:
                        count += 1

                cc = 0
                for x in range(r-1, -1, -1):
                    if g[x][j] == 1:
                        cc += 1
                    else:
                        break
                    #print(rc, cc)
                    if cc == 2*rc or rc == 2*cc:
                        count += 1
    print("2th", count)
    for i in range(c):
        rc = 0
        for j in range(r):
            if g[j][i] == 1:
                rc += 1
            else:
                rc = 0
            if rc > 2:
                print("3rd ", 'one seg found', i, j, rc)
                cc = 0
                for x in range(i, c):
                    if g[j][x] == 1:
                        cc += 1
                    else:
                        break
                    print("3dr col row count", rc, cc)
                    if cc == 2*rc or rc == 2*cc:
                        count += 1

                cc = 0
                for x in range(c-1, -1, -1):
                    if g[j][x] == 1:
                        cc += 1
                    else:
                        break
                    #print(rc, cc)
                    if cc == 2*rc or rc == 2*cc:
                        count += 1
    print("3th", count)
    for i in range(c):
        rc = 0
        for j in range(r-1, -1, -1):
            if g[j][i] == 1:
                rc += 1
            else:
                rc = 0
            if rc > 2:
                #print('one seg found', i)
                cc = 0
                for x in range(i, c):
                    if g[j][x] == 1:
                        cc += 1
                    else:
                        break
                    #print(rc, cc)
                    if cc == 2*rc or rc == 2*cc:
                        count += 1

                cc = 0
                for x in range(c-1, -1, -1):
                    if g[j][x] == 1:
                        cc += 1
                    else:
                        break
                    #print(rc, cc)
                    if cc == 2*rc or rc == 2*cc:
                        count += 1

    print("4th", count)
