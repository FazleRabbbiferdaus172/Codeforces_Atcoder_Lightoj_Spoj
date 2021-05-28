for _ in range(int(input())):
    n = int(input())
    l = sorted(list(map(int, input().split())), reverse=True)
    ans = [0]*(2*n)
    for i, j in enumerate(l):
        if i < n:
            ans[2*i+1] = j
        else:
            x = n - i
            ans[2*x] = j
    print(*ans)
