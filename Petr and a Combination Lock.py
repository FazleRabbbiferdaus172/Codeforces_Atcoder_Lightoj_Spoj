n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))


a.sort()

s = 0

for i in a:
    if s - i == 0:
        s -= i
    else:
        s += i
if s == 0:
    print("YES")
elif sum(a) % 360 == 0:
    print("YES")
else:
    print("NO")
