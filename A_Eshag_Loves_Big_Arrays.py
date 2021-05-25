for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    min_ele = min(l)
    min_count = l.count(min_ele)
    ans = n - min_count
    print(ans)
