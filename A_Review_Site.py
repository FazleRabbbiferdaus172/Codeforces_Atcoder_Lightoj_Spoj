for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = l.count(1) + l.count(3)
    print(ans)
