for _ in range(int(input())):
    n = int(input())
    a = [0]*(n+1)
    l = map(int, input().split())
    for i in l:
        a[i] += 1

    print(max(a))
