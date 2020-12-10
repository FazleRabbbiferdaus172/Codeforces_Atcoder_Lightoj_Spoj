l = []
for _ in range(4):
    l.append(int(input()))
d = int(input())
mark = [0]*(d+1)
for i in l:

    for j in range(i, d+1, i):
        mark[j] = 1

print(mark.count(1))
