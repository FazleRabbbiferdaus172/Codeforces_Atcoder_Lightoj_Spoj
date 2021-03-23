"""
ID: fazle.f1
LANG: PYTHON3
TASK: gift1
"""
fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

n = int(fin.readline())
d = {}
for i in range(n):
    x = fin.readline()
    d[x] = 0
for i in range(n):
    x = fin.readline()
    a, b = map(int, fin.readline().split())
    if b == 0:
        c = 0
    else:
        c = a//b

    d[x] -= c * b
    #print("c:", c, "d:", d[x])
    # print("giving")
    for i in range(b):
        x = fin.readline()
        d[x] += c
        #print("giving ", d)

for i in d:
    fout.write(str(i.strip())+" "+str(d[i])+"\n")
