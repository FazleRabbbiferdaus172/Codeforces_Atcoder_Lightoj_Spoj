for _ in range(int(input())):
    n, d = map(int, input().split())
    l = list(map(int, input().split()))

    ans = "NO"

    for i in range(n):
        for j in range(n):
            if i != j:
                if l[i] + l[j] <= d:
                    ans = "YES"
                    break

    if ans == 'NO':
        for i in l:
            if i > d:
                break
        else:
            ans = "YES"

    print(ans)
