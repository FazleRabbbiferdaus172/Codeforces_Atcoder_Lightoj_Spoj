for _ in range(int(input())):
    n, a, b = map(int, input().split())
    c = 1
    while True:
        if n < c:
            print('No')
            break
        if (n-c) % b == 0:
            print('Yes')
            break
        else:
            c *= a
        if a == 1:
            print('No')
            break
