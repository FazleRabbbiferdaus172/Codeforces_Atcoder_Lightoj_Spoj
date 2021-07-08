for _ in range(int(input())):
    n, x = map(int, input().split())
    ans = 1
    if n > 2:
        ans += (n - 2) // x
        if (n - 2) % x:
            ans += 1
    print(ans)
