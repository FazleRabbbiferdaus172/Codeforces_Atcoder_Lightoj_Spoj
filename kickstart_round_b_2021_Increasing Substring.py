for t in range(int(input())):
    n = int(input())
    s = input()
    #s = s[::-1]
    count = 1
    m = 1
    ans = [0]*n
    ans[0] = 1
    for i in range(1, n):
        if s[i] > s[i-1]:
            count += 1
            m = max(m, count)
            ans[i] = m
        else:
            m = 1
            count = 1
            ans[i] = m

    m = max(m, count)
    ans[n-1] = m

    print("Case #{}:".format(t+1), *ans)
