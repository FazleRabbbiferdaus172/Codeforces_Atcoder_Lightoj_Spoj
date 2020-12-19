for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))

    s = sum(x)
    cur = [0, 0]
    for i in range(n):
        cur[i % 2] += x[i] - 1
    #print(*cur, s)
    for j in range(2):
        if 2*cur[j] > s:
            continue

        for i in range(n):
            if i % 2 == j:
                x[i] = 1
                # print(i)
        break
    print(*x)
