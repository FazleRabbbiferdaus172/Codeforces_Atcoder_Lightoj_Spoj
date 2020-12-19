for _ in range(int(input())):
    n = int(input())
    red = list(input())
    blue = list(input())

    rmore, bmore = 0, 0

    for i in range(n):
        if int(red[i]) > int(blue[i]):
            rmore += 1
        elif int(blue[i]) > int(red[i]):
            bmore += 1

    if rmore > bmore:
        print("RED")
    elif bmore > rmore:
        print("BLUE")
    else:
        print("EQUAL")
