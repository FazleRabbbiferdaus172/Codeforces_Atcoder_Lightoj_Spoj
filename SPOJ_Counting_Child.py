for t in range(1, int(input())+1):
    n = int(input())
    l = list(map(int, input().split()))
    ans = [0]*(n+1)
    # print(ans)
    opend = []
    for i in l:
        if len(opend) > 1 and opend[-1] == i:
            # print(opend[-1])
            ans[opend[-2]] += 1
            opend.pop(-1)
        else:
            opend.append(i)

    print("Case {}:".format(t))
    for i in range(1, n+1):
        print("{} -> {}".format(i, ans[i]))
    print()
