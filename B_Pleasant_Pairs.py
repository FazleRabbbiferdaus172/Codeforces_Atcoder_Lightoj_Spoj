for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(l[i]-i-2, n, l[i]):
            if l[i]*l[j] == i+j+2 and i < j:
                c += 1
    print(c)
