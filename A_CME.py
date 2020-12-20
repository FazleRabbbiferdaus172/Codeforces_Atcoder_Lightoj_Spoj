for i in range(int(input())):
    n = int(input())

    if n/2 == n//2:
        ans = 0
    else:
        ans = 1

    if n == 2:
        ans = 2

    print(ans)
