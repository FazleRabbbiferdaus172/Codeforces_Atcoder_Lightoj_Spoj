n = int(input())

l = list(map(int, input().split()))

oh = l.count(100)
th = n - oh

if oh % 2 == 1:
    print("NO")
elif oh == 0 and th % 2 == 1:
    print("NO")
else:
    print("YES")
