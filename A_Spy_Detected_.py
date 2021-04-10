for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = -1
    for i in range(n):
        if l.count(l[i]) == 1:
            ans = i
            break
    print(ans+1)
