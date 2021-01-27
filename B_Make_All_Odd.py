for _ in range(int(input())):
    n = input()
    l = list(map(int, input().split()))

    l = [i % 2 for i in l]
    if not 1 in l:
        print(-1)
    else:
        print(l.count(0))
