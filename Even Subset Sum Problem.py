for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    lx = [x % 2 for x in l]
    if lx.count(0) > 0:
        print(1)
        print(lx.index(0)+1)
    else:
        if lx.count(1) >= 2:
            print(2)
            print(1, 2)
        else:
            print(-1)
