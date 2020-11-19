for _ in range(int(input())):
    l = list(input())

    front_1 = []
    front_2 = []
    a, b, c = 0, 0, 0
    for i in l:
        if i == '[':
            a += 1
        elif i == '(':
            b += 1
        elif i == ']' and a > 0:
            a -= 1
            c += 1
        elif i == ')' and b > 0:
            b -= 1
            c += 1
        #print("test", a, b, c)

    print(c)
