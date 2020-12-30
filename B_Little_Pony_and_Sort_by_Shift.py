n = int(input())
l = list(map(int, input().split()))
for i in range(1, n):
    if l[i-1] > l[i]:
        print((-1, n-i)[sorted(l) == l[i:]+l[:i]])
        break
else:
    print(0)
