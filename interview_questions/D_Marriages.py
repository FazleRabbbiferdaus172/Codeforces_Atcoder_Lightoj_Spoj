
for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))

    ans = [0] * n
    taken = [0] * n
