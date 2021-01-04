for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    ans = [0]*n

    for i in range(n-1, -1, -1):
        #print(i + l[i])
        if i + l[i] >= n:
            ans[i] = l[i]
        else:
            x = l[i]
            ans[i] = l[i] + ans[i+x]
        # print(ans)

    print(max(ans))
