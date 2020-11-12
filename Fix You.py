for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]

    x = []
    for i in range(n):
        x.append(input())
    # print(x)
    ans = 0
    for i in range(n-1):
        if x[i][-1] == 'R':
            ans += 1

    for i in range(m-1):
        if x[-1][i] == 'D':
            ans += 1

    print(ans)
