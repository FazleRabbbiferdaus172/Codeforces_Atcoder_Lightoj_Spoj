inf = open("input.txt", 'r')
ouf = open("output.txt", 'w')
n = int(inf.readline())
l = list(map(int, inf.readline().split()))
d = dict()

for j, i in enumerate(l):
    if i in d:
        d[i] += [j+1]
    else:
        d[i] = [j+1]

ans = []

for i in d:
    if len(d[i]) % 2 != 0:
        ouf.write(str(-1)+"\n")
        break
    ans += d[i]
else:
    for i in range(0, len(ans), 2):
        ouf.write(str(ans[i])+" "+str(ans[i+1])+"\n")
