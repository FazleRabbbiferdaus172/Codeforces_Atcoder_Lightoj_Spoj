import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = list(map(int, input().split()))
ul = [0]*n
ul[-1] = 1
d = {l[-1]: 1}

for i in range(n-2, -1, -1):
    if not l[i] in d:
        d[l[i]] = 1
        ul[i] = ul[i+1] + 1
    else:
        ul[i] = ul[i+1]
for i in range(m):
    x = int(input())
    x -= 1
    print(ul[x])
