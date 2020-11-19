for _ in range(int(input())):
    x, y = map(int, input().split())

    ans = x+y

    if max(x, y) - 1 > min(x, y):
        ans += max(x, y) - min(x, y) - 1

    print(ans)
