inf = open("input.txt", 'r')
ouf = open("output.txt", 'w')
n, m = map(int, inf.readline().split())
ss = ""
i = 0
f, s = "B", "G"
if n < m:
    f = "G"
    s = "B"
    n, m = m, n

while n > 0 and m > 0:
    if i % 2 == 0:
        ss += f
        n -= 1
    else:
        ss += s
        m -= 1
    i += 1

ss += f*n
ss += s*m
ouf.write(ss)
