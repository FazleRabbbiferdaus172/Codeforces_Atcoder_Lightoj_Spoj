def dfs(r, p):
    global cost, visit, adj, ans

    visit[r] = 1
    if cost[p][r] != 0:
        ans[0] += 0
    else:
        ans[0] += cost[r][p]

    if cost[r][p] != 0:
        ans[1] += 0
    else:
        ans[1] += cost[p][r]

    #print(r, "->", end="")
    for i in adj[r]:
        if visit[i] != 1:
            dfs(i, r)


for tt in range(int(input())):
    input()
    n = int(input())
    adj = [[] for i in range(n)]
    cost = [[0]*n for i in range(n)]
    for i in range(n):
        a, b, c = map(int, input().split())
        adj[a-1] += [b-1]
        adj[b-1] += [a-1]
        cost[a-1][b-1] = c

    # print(adj)
    # print(cost)
    ans = [0, 0]
    visit = [0]*n
    cc = dfs(0, n-1)
    print("Case {}: {}".format(tt+1, min(ans)))
