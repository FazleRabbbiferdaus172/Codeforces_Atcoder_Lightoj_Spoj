n, m = map(int, input().split())

l = list(map(int, input().split()))

l.sort()

diff = []

for i in range(m-n+1):
    #print(l[i], l[i+n-1], )
    diff += [l[i+n-1] - l[i]]
print(min(diff))
