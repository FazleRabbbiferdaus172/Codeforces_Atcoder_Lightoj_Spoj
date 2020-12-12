for _ in range(int(input())):
    n, k = map(int, input().split())

    xx = "abc"

    ll = n//3
    kk = n % 3

    print(xx*ll + xx[:kk])
