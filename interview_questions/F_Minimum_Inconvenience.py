for _ in range(int(input())):
    n = int(input())
    a = sum(list(map(int, input().split())))
    ex = a % n
    ans = ex*(n-ex)
    print(ans)
