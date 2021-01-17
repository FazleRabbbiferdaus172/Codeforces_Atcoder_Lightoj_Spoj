import math
s = input()
d = dict()
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
x = [d[i] % 2 for i in d]
n = x.count(1)
if n <= 1:
    n = 1

ans = ["Second", "First"]
print(ans[n % 2])

# Editorial
