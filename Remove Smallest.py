t = int(input())

for q in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    c = 0
    for i in range(0, n-1):
        j = i+1
        if abs(a[i]-a[j]) <= 1:
            a[a.index(min(a[i], a[j]))] = 105
    if n - a.count(105) == 1:
        print("YES")
    else:
        print("NO")
