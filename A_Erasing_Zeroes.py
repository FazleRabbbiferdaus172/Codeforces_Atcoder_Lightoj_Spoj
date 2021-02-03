for _ in range(int(input())):
    s = list(input())

    while s and s[0] == '0':
        s.pop(0)

    while s and s[-1] == '0':
        s.pop(-1)

    c = 0

    for i in s:
        if i == '0':
            c += 1
    print(c)
