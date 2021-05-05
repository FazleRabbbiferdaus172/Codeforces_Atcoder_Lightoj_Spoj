for _ in range(int(input())):
    n = input()
    l = list(map(int, input().split()))
    odd, even = [], []
    for i in l:
        if i % 2:
            odd += [i]
        else:
            even += [i]
    ans = odd + even
    print(*ans)
