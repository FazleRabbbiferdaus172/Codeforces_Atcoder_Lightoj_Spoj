for t in range(int(input())):
    n = int(input())
    ans = 1
    l = list(map(int, input().split()))
    ans = min(l) * max(l)
    print("Case {}: {}".format(t+1, int(ans)))
