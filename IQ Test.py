l = []
for _ in range(4):
    l.append(input())
res = False
for _ in range(3):
    for i in range(3):
        for j in range(3):
            x = l[i][j:j+2]
            y = l[i+1][j:j+2]
            a, b = x.count('#'), x.count('.')
            c, d = y.count('#'), y.count('.')
            # print(i)
            # print(x)
            # print(y)
            #print(a, b)
            #print(c, d)
            # print("ok")
            if a+c >= 3 or b+d >= 3:
                res = True
                break
if res:
    print("YES")
else:
    print("NO")
