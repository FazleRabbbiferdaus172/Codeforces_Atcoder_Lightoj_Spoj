'''
def bfs(r):
    global g, vis, child
    q = [r]

    while q:
        temp = q.pop(0)
        # print(temp)
        # print(q)
        if vis[temp] == 1:
            continue
        vis[temp] = 1
        #print(temp, end="->")
        for i in g[temp]:

            if vis[i]:
                continue
            q.append(i)
            #vis[i] = 1
            #print(temp, i)
            #print(temp, i, vis[i])
            child[temp] += 1
            child[i] += 1
    print(child)

    if 1 in child:
        send = 1
    else:
        send = 0

    for i in range(1, n+1):
        if child[i] == 1:
            if not g[i]:
                continue
            x = g[i].pop()
            g[x].remove(i)
    # print(g)
    return send
'''

n, m = map(int, input().split())
g = {}
deg = [0]*(n+1)
for i in range(1, n+1):
    g[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]
    deg[a] += 1
    deg[b] += 1

# print(g)
'''vis = [0]*(n+1)
vis[0] = [-1]
child = [0]*(n+1)
ans = 0
for i in range(1, n+1):
    # if not vis[i]:
    #print("called with", i)
    vis = [0]*(n+1)
    vis[0] = [-1]
    child = [0]*(n+1)
    ans += bfs(i)
print(ans)
'''
ans = 0
for _ in range(1, n+1):
    r = []
    for i in range(1, n+1):
        if deg[i] == 1:
            r += [i]
            deg[i] = 0
    if not r:
        break
    ans += 1
    for i in range(1, n+1):
        if deg[i] >= 2:
            for j in r:
                if j in g[i]:
                    deg[i] -= 1
print(ans)
