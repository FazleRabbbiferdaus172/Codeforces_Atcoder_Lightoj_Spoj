n = int(input())

N = n+2
mark = [1]*N


for i in range(2, N):
    if mark[i] == 1:
        for j in range(i*i, N, i):
            mark[j] = 2

print(len(set(mark[2:])))
print(*mark[2:])
