for i in range(int(input())):
    s = [len(x) for x in input().split('0')]
    s.sort(reverse=True)
    ans = 0
    for i in range(0, len(s), 2):
        ans += s[i]
    print(ans)
