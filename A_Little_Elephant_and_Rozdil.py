n = int(input())

l = list(map(int, input().split()))
x = min(l)

if l.count(x) > 1:
    print("Still Rozdil")
else:
    print(l.index(x)+1)
