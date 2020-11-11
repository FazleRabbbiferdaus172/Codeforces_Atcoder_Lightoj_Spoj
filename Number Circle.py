n = int(input())

l = [int(x) for x in input().split()]
l.sort()
if l[-1] >= l[-2] + l[-3]:
    print("NO")
else:
    print("YES")
    for i in range(n-1, -1, -2):
        print(l[i], end=" ")
    for i in range(n % 2, n, 2):
        print(l[i], end=" ")
    print()
