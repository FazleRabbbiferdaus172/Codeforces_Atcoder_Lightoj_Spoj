for _ in range(int(input())):
    n = int(input())

    s = list(input())
    #x = len(s)
    c = 0
    while len(s) and s[-1] == ')':
        c += 1
        s.pop(-1)
    # print(c)
    if c > n-c:
        print("Yes")
    else:
        print("No")
