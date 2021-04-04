for _ in range(int(input())):
    n = int(input())
    s = list(input())
    t = list(input())
    am = [0]*n
    zC, oC = 0, 0
    for x, i in enumerate(s):
        if i == '0':
            zC += 1
        else:
            oC += 1

        if oC == zC:
            am[x] = 1
        else:
            am[x] = 0
    done = 0
    for i in range(-1, -n-1, -1):

        if done % 2 == 0 and s[i] != t[i] and am[i] != 1:
            print("NO")
            break
        elif done % 2 == 1 and s[i] == t[i] and am[i] != 1:
            print("NO")
            #print("chk", s[i], abs(int(t[i]) - 1), am[i])
            break
        elif done % 2 == 0 and s[i] != t[i] and am[i] == 1:
            #print("1inc", i)
            done += 1
        elif done % 2 == 1 and s[i] == t[i] and am[i] == 1:
            #print("2inc", i)
            done += 1
    else:
        print("YES")
