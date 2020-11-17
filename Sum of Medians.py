import math
for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    l.sort(reverse=True)
    move = math.ceil(n/2)
    move = n - move + 1
    ans = []
    for i in range(move-1, len(l), move):
        #print(i, l[i])
        ans.append(l[i])
    ans.sort(reverse=True)
    print(sum(ans[0:k]))
