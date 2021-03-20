for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ss = s[:k] + s[n-k:n]
    #print(s[:k], s[n-k:n])
    if n != 2*k and ss == ss[::-1]:
        print("YES")
    else:
        print("NO")
