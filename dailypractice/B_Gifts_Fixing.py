for i in range(int(input())):
    n = int(input())
    cand = list(map(int, input().split()))
    apple = list(map(int, input().split()))
    c = min(cand)
    a = min(apple)
    ans = 0
    for i in range(n):
        s_c, s_a = cand[i] - c, apple[i] - a
        ans += max(s_c, s_a)

    print(ans)
