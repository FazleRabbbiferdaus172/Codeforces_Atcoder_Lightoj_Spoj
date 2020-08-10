t = int(input())

for ti in range(t):
    n = int(input())
    l = list()
    d = dict()
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        l.append([a, b])
        if a+b in d:
            d[a+b] += 1
        else:
            d[a+b] = 1

    l.sort()
    if d[max(d, key=d.get)] > 1:
        print("NO")
    else:
        # print("YES")
        a = "YES"
        prvr, prvu = 0, 0
        s = ''
        for i in l:
            s += 'R'*(i[0]-prvr) + 'U'*(i[1] - prvu)
            if i[0]-prvr < 0 or i[1] - prvu < 0:
                a = "NO"
                break
            prvr, prvu = i[0], i[1]
        if a == "NO":
            print(a)
        else:
            print(a)
            print(s)
