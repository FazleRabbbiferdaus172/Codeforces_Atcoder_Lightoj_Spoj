n = int(input())
l = [int(x) for x in input().split()]

s = set(l)

m = float('-inf')

for i in s:
    m = max(m, l.count(i))

if n >= m+(m-1):
    print("YES")
else:
    print("NO")
