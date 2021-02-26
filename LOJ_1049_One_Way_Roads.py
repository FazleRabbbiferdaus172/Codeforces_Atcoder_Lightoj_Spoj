def dfs(r, p):
    global cost, visit, adj, ans, lst

    visit[r] = 1
    lst = r
    if p != None:
        if cost[p][r] == 0:
            ans[0] += cost[r][p]

        if cost[r][p] == 0:
            ans[1] += cost[p][r]

    #print("cur:", r, "par:", p, "cost: ", *ans, "->")
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
    lst = None
    ans = [0, 0]
    visit = [0]*n
    cc = dfs(0, None)
    if cost[lst][0] == 0:
        ans[0] += cost[0][lst]

    if cost[0][lst] == 0:
        ans[1] += cost[lst][0]
    # print(*ans)
    print("Case {}: {}".format(tt+1, min(ans)))
