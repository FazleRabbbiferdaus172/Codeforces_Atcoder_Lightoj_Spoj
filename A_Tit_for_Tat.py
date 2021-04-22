for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    x = 0
    while x < n and k:
        while x < n - 1 and l[x] <= 0:
            x += 1
        l[x] -= 1
        l[-1] += 1
        k -= 1

    print(*l)
