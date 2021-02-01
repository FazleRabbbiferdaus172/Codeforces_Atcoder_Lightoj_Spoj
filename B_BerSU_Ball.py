n = int(input())
b = list(map(int, input().split()))
m = int(input())
g = list(map(int, input().split()))

b.sort()
g.sort()
c = 0
for i in b:
    for j in range(m):
        if abs(i-g[j]) <= 1:
            c += 1
            g[j] = 1000
            break


print(c)
