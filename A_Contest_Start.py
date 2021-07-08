for i in range(int(input())):
    n, x, t = map(int, input().split())
    ans = max(0, n-t//x) * (t//x) + min(n-1, t//x - 1) * min(n, t//x)//2
    print(ans)
