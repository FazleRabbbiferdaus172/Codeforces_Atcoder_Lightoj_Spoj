for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if l == sorted(l):
        print(0)
    elif l[0] == n and l[-1] == 1:
        print(3)
    elif l[0] == 1 or l[-1] == n:
        print(1)
    else:
        print(2)
