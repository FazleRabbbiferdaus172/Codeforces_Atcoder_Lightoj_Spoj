for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    s1, s2 = s[0:n//2], s[n//2:]
    s2 = s2[::-1]
    #print(s1, s2)
    has = 0
    for i in range(n//2):
        if s1[i] != s2[i]:
            has += 1
    ans = abs(k - has)
    print("Case #{}: {}".format(t+1, ans))
