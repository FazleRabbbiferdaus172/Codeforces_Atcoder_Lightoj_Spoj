for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]

    ans = n * (k//(n-1)) + (k % (n-1))

    if k % (n-1) == 0:
        ans -= 1

    print(ans)
