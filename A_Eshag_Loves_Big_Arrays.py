for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    x = l.count(min(l))
    print(n-x)
