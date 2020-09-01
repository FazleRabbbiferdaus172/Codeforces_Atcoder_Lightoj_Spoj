t = int(input())
for _ in range(t):
    n = input()
    l = [int(x) % 2 for x in input().split()]
    if l.count(0) == len(l):
        print("NO")
    elif l.count(1) == len(l) and len(l) % 2 == 0:
        print("NO")
    else:
        print("YES")
