n = int(input())

top = int(input())
bottom = 7 - top
s = [int(x) for x in input().split()]
can = True
for _ in range(n-1):
    s = [int(x) for x in input().split()]
    if bottom in s or top in s:
        can = False
    else:
        top = bottom
        bottom = 7 - top

if can:
    print("YES")
else:
    print("NO")
