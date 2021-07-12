for _ in range(int(input())):
    n = int(input())
    ans = [0]*n
    for i in range(0, n):
        if i % 2 == 0:
            ans[i] = i+2
        else:
            ans[i] = i
    if n % 2 == 1:
        ans[-1], ans[-2] = ans[-2], n
    print(*ans)
