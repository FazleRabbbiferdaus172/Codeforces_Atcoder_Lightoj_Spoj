for _ in range(int(input())):
    n = int(input())

    l = list(map(int, input().split()))

    l = [i % 2 for i in l]

    if l.count(1) != n//2:
        print(-1)
    else:
        c = 0

        for i in range(n):
            if i % 2 == 0 and l[i] == 1:
                c += 1

        print(c)
