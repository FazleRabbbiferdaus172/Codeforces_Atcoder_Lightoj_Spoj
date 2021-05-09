while True:
    v, e = map(int, input().split())
    if v == 0 and e == 0:
        break
    cost = list(map(int, input().split()))
    g = {}
    for i in range(v):
        g[i+1] = []
    for _ in range(e):
        a, b = map(int, input().split())
        g[b] += [a]
    nq = int(input())
    query = list(map(int, input().split()))
    input()
    print(g)
