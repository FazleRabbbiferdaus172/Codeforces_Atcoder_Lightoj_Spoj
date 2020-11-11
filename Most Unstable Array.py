for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(2*m)
