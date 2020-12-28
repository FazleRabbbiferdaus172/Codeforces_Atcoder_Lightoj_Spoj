for _ in range(int(input())):
    n = int(input())
    rb = list(map(int, input().split()))
    m = int(input())
    bb = list(map(int, input().split()))
    ans = 0
    m = 0
    for i in rb:
        ans += i
        m = max(ans, m)
    ans = m
    #print("mid", ans)
    for i in bb:
        ans += i
        m = max(ans, m)

    print(m)
