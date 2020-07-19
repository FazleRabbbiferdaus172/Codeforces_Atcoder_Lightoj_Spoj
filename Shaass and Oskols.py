n = int(input())
w_n = [int(x) for x in input().split()]
m = int(input())
x_y = []
for i in range(m):
    l = [int(x) for x in input().split()]
    x_y.append(l)

for i in x_y:
    if i[0] == 1:
        if i[0] == n:
            w_n[i[0]-1] = 0
            continue
        w_n[i[0]] += w_n[i[0]-1]-i[1]
        w_n[i[0]-1] = 0
    elif i[0] == n:
        w_n[i[0]-2] += i[1]-1
        w_n[i[0]-1] = 0
    else:
        w_n[i[0]-2] += i[1]-1
        w_n[i[0]] += w_n[i[0]-1]-i[1]
        w_n[i[0]-1] = 0

for i in w_n:
    print(i)
