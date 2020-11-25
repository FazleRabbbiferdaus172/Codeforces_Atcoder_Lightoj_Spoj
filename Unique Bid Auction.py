import sys
input = sys.stdin.readline
for _ in range(int(input().strip())):
    n = int(input().strip())
    oc = [0]*(n+1)
    l = list(map(int, input().split()))
    for i in l:
        oc[i] += 1

    if 1 in oc:
        print(l.index(oc.index(1))+1)
    else:
        print(-1)
