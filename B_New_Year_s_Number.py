for _ in range(int(input())):
    n = int(input())
    if n < 2020:
        print("NO")
    else:
        r = n % 2020
        d = n // 2020
        if r <= d:
            print("YES")
        else:
            print("NO")
