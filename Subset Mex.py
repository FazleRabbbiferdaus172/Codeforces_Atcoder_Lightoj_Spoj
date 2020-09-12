t = int(input())

for _ in range(t):
    n = input()
    l = [int(x) for x in input().split()]

    l.sort()

    a, b = 0, 0
    for i in l:
        if i == a:
            a += 1

        elif i == b:
            b += 1

    print(a+b)
