
def bfs(r):
    global g, vis, child
    q = [r]

    while q:
        temp = q.pop(0)
        vis[temp] = 1
        #print(temp, end="->")
        for i in g[temp]:
            if vis[i]:
                continue
            q.append(i)
            child[temp] += 1
            child[i] += 1
    print(child)
    x = 0
    if 1 in child:
        x = max(child)
    # print(x)
    child = [0]*(n+1)
    return x


n, m = map(int, input().split())
g = {}
for i in range(1, n+1):
    g[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a] += [b]
    g[b] += [a]

# print(g)
vis = [0]*(n+1)
vis[0] = [-1]
child = [0]*(n+1)
ans = 0
for i in range(1, n+1):
    if not vis[i]:
        #print("called with", i)
        ans += bfs(i)
print(ans)
