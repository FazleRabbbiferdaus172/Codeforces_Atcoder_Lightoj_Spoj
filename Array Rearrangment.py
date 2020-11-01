te = int(input())
for j in range(te):
    n, x = [int(z) for z in input().split()]

    o = [int(z) for z in input().split()]
    t = [int(z) for z in input().split()]

    o.sort()
    t.sort(reverse=True)
    ans = []
    for i in range(n):
        ans.append(o[i]+t[i])

    if max(ans) <= x:
        print("Yes")
    else:
        print("No")

    if j <= te - 2:
        dum = input()
