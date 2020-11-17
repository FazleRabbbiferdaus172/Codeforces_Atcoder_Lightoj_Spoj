for _ in range(1):
    n = input()
    l = list(map(int, input().split()))
    m = l[0]
    ans = []
    ans.append(m)
    for i in l[1:]:
        ans.append(i+m)
        m = max(m, ans[-1])

    print(*ans)
