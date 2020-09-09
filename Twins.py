n = int(input())
l = [int(x) for x in input().split()]
l.sort(reverse=True)
s = sum(l)
for i in range(0, n):
    sa = sum(l[:i+1])
    if (sa > s-sa):
        print(i+1)
        break
