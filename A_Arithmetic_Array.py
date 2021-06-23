for _ in range(int(input())):
    n = int(input())
    l = sum(list(map(int, input().split())))
    if l < n:
        print(1)
    else:
        print(l - n)
