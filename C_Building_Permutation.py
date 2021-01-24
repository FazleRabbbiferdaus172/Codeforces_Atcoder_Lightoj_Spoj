n = int(input())
l = list(map(int, input().split()))
c = 0
l.sort()
for i in range(n):
    c += abs((i+1) - l[i])
print(c)
