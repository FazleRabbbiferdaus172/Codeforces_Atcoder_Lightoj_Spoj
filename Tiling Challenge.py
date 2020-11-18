n = int(input())

l = []

for _ in range(n):
    x = list(input())
    # print(x)
    l.append(x)
# print(l)
flag = True
for x, i in enumerate(l):
    for y, j in enumerate(i):

        if y == 0 and j == '.':
            flag = False
            break
        elif y == n-1 and j == '.':
            flag = False
            break
        elif x >= n-2 and j == '.':
            flag = False
            break
        elif j == '.' and (l[x+1][y] != '.' or l[x+1][y+1] != '.' or l[x+1][y-1] != '.' or l[x+2][y] != '.'):
            flag = False
            break
        elif j == '.':
            #print(x, y)
            l[x][y] = '#'
            l[x+1][y] = '#'
            l[x+1][y+1] = '#'
            l[x+1][y - 1] = '#'
            l[x+2][y] = '#'
            # print(l)
# print(l)
if not flag:
    print("NO")
else:
    print("YES")
