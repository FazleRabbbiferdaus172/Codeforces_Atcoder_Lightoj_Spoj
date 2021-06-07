for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    i = 0
    ans = 0
    for i in l:
        if i < 0:
            ans = 1
            break
    if ans:
        print("NO")
    else:
        print("YES")
        print("101")
        l = range(0, 101)
        print(*l)
