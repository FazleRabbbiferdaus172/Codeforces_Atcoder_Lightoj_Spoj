for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = n//k
    ans = ans*k
    ans += min(k//2, n-ans)

    print(ans)
