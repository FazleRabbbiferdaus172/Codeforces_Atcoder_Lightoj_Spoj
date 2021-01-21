n = int(input())
d = list(map(int, list(input())))

s1, s2 = d[:n], d[n:]
s1.sort()
s2.sort()
less, more = True, True

for i in range(n):
    if s1[i] >= s2[i]:
        less = False
        break
for i in range(n):
    if s1[i] <= s2[i]:
        more = False
        break

if less == True or more == True:
    print("YES")
else:
    print("NO")
