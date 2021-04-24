for _ in range(int(input())):
    n = int(input())
    ans = n // 2050
    rem = n % 2050
    if rem:
        ans = -1
    else:
        ans = sum(list(map(int, str(ans))))
    print(ans)
