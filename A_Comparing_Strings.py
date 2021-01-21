import sys
s1 = list(input())
s2 = list(input())
d1, d2 = dict(), dict()
miss = 0
if len(s1) != len(s2):
    print("NO")
    sys.exit(0)
for i in range(97, 97+26):
    d1[chr(i)] = 0
    d2[chr(i)] = 0

for i in range(len(s1)):
    d1[s1[i]] += 1
    d2[s2[i]] += 1
    if s1[i] != s2[i]:
        miss += 1

if d1 == d2 and miss == 2:
    print("YES")
else:
    print("NO")
