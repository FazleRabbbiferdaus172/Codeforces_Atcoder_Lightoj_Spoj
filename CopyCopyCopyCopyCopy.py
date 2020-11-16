for _ in range(int(input())):
    n = int(input())

    l = set(map(int, input().split()))

    print(min(n, len(l)))
