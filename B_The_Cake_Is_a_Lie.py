'''
#Helped me to find the answer **thank you brute force**
for _ in range(int(input())):
    fx, fy, m = map(int, input().split())
    amount = 0

    move = [(0, 1), (1, 0)]
    visited = []
    root = (1, 1, 0)
    q = [root]
    ans = "NO"
    while q:
        node = q.pop(0)
        # print(len(q))
        visited.append(node)
        if node == (fx, fy, m):
            ans = "YES"
            break
        for i in move:
            x = node[0] + i[0]
            y = node[1] + i[1]
            if i[0]:
                a = node[-1] + node[1]
            elif i[1]:
                a = node[-1] + node[0]
            ch = (x, y, a)
            if ch in visited:
                continue
            if ch in q:
                continue
            elif ch[0] > fx or ch[1] > fy or ch[2] > m:
                continue
            else:
                print("ch", ch)
                q.append(ch)
    print(ans)
'''

for _ in range(int(input())):
    fx, fy, m = map(int, input().split())
    if fx*fy - 1 == m:
        print("YES")
    else:
        print("NO")
