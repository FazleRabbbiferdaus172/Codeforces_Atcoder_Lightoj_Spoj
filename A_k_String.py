import sys
n = int(input())
s = input()
d = dict()

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1


k = list(d.keys())
v = list(d.values())
s = ""
for i in k:
    if d[i] >= n and d[i] % n == 0:
        a = i*(d[i]//n)
        s += a
    else:
        print("-1")
        break
else:
    print(s*n)
#print(k, v)
