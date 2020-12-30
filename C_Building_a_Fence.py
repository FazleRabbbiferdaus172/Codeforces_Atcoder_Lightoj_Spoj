for _ in range(int(input())):
    n, k = map(int, input().split())

    h = list(map(int, input().split()))

    base, top = h[0], h[0]
    ans = True
    for i in range(1, n):
        base = max(base - k + 1, h[i])
        top = min(top+k-1, h[i] + k - 1)
        #print(base, top)
        if base > top:
            ans = False
            break

    if h[n-1] < base or h[n-1] > top:
        ans = False

    if ans:
        print("YES")
    else:
        print("NO")
