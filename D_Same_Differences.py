for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(n):
        temp = l[i] - i
        if not temp in d:
            d[temp] = 0
        ans += d[temp]
        d[temp] += 1
    print(ans)
