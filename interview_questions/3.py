m = int(input())
seat = list(map(int, input().split()))
alien = list(input())
seat = sorted([[i, ind+1] for ind, i in enumerate(seat)])
free = []
start = 0
for i in alien:
    if i == '0':
        free += [seat[start]]
        print(seat[start][1], end=" ")
        start += 1
    else:
        ans = free.pop(-1)
        print(ans[1], end=" ")
