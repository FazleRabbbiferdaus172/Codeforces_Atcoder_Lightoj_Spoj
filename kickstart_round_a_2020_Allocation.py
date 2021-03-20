for t in range(int(input())):
    n, k = map(int, input().split())
    l = sorted(list(map(int, input().split())))
    count = 0
    for i in l:
        if i <= k:
            k -= i
            count += 1
    print("Case #{}: {}".format(t+1, count))
