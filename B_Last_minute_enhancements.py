import sys
input = sys.stdin.readline

for i in range(int(input().strip())):
    n = int(input().strip())
    l = list(map(int, input().split()))
    c = 1
    for i in range(1, n):
        if l[i] == l[i-1]:
            l[i] += 1
            c += 1
        elif l[i] < l[i-1]:
            l[i] += 1
        elif l[i] > l[i-1]:
            c += 1
    print(c)
