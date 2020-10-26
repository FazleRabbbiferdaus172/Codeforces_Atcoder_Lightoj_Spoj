
for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]

    ans = []
    for i in range(n-1, -1, -1):
        if(i % 2 == 0):
            ans.append(l[i]*-1)
        else:
            ans.append(l[i])
    print(*ans)
