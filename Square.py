for _ in range(int(input())):
    l = list(map(int, input().split()))
    ll = list(map(int, input().split()))

    l.sort()
    ll.sort()

    if l[0]+ll[0] == l[1] and l[0]+ll[0] == ll[1]:
        print("Yes")
    else:
        print("No")
