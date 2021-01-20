import sys
n = int(input())
l = list(map(int, input().split()))

if 5 in l or 7 in l:
    print(-1)
elif 3 in l and not 6 in l:
    print(-1)
else:
    d = {1: 0, 2: 0, 3: 0, 4: 0, 6: 0}
    for i in l:
        d[i] += 1
    ans = []
    for i in range(n//3):

        if d[1] > 0 and d[2] > 0 and d[4] > 0:
            x = [1, 2, 4]
            d[1] -= 1
            d[2] -= 1
            d[4] -= 1
        elif d[1] > 0 and d[3] > 0 and d[6] > 0:
            x = [1, 3, 6]
            d[1] -= 1
            d[3] -= 1
            d[6] -= 1
        elif d[1] > 0 and d[2] > 0 and d[6] > 0:
            x = [1, 2, 6]
            d[1] -= 1
            d[2] -= 1
            d[6] -= 1
        else:
            continue

        ans.append(x)

    if d[1] > 0 or d[2] > 0 or d[3] > 0 or d[4] > 0 or d[6] > 0:
        print(-1)
    else:
        for i in ans:
            print(*i)
