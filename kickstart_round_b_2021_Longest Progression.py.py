
for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = [0]*n
    ans[0] = 1
    adif = [l[0] - l[1]]
    sdif = l[0] - l[1]
    for i in range(1, n):
        dif = l[i-1] - l[i]
        adif.append(dif)
        if dif == sdif:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = 1
        sdif = dif
    ans_x = max(ans)
    for i in range(1, n):
        if adif[i] != adif[i-1]:
            add_sub = adif[i] - adif[i-1]
            x = l[i-1] - (l[i] + add_sub)
            y = l[i-1] - (l[i] - add_sub)
            if x == adif[i-1]:
                send = l[i] + add_sub
            elif y == adif[i-1]:
                send = l[i] - add_sub
            # print(send)
            temp = ans[i-1] + 1
            if i+1 < n and adif[i-1] == send - l[i+1]:
                #print("yes", temp)
                for j in range(i+1, n):
                    if j == i+1:
                        temp += 1
                        continue
                    #print("chk", j, ":", adif[i-1], adif[j])
                    if adif[i-1] == adif[j]:
                        temp += 1
                    else:
                        break
            ans_x = max(temp, ans_x)

    print("Case #{}:".format(t+1), ans_x)
    #print("ans_x", ans_x)
    # print(*adif)
