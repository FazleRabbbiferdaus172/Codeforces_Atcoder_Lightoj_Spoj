for _ in range(int(input())):
    n = input()
    l = list(map(int, input().split()))
    i = 0
    while l:
        if i % 2 == 0:
            x = l.pop(0)
        else:
            x = l.pop(-1)
        print(x, end=" ")
        i += 1
    print()
