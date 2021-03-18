n = int(input())
l = list(map(int, input().split()))
g = [[] for i in range((n))]
j = 0
for i in l:
    g[j].append(i - 1)
    j += 1
print(g)

vis = [0]*n


def dfs(g, x):
    global vis
    vis[x] = 1
    print(x)
    for i in g[x]:
        if vis[i] == 1:
            continue
        dfs(g, i)


for i in range(n):
    vis = [0]*n
    dfs(g, i)
    print('end')
