for _ in range(int(input())):
    l = [int(x) for x in input().split()]
    l.sort()
    if l[0] >= 4:
        print(7)
    elif l[0] == 3:
        print(6)
    elif l[0] == 2:
        if l[1] >= 2 and l[2] >= 3:
            print(5)
        else:
            print(4)
    elif l[0] == 1:
        if l[1] >= 2:
            print(4)
        else:
            print(3)
    else:
        if l[2] == 0:
            print(0)
        elif l[1] >= 2:
            print(3)
        elif l[1] == 1:
            print(2)
        else:
            print(1)
