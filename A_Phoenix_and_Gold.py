for _ in range(int(input())):
    n, x = map(int, input().split())
    w = list(map(int, input().split()))
    w.sort()
    ans = []
    total = 0
    temp = None
    for i in w:
        total += i
        if total == x:
            temp = i
            continue
        ans += [i]
    if temp != None:
        ans += [temp]
    if sum(w) == x:
        print("NO")
    else:
        print("YES")
        print(*ans)
