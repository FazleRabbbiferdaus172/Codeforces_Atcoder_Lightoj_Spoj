n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x, y = max(a), min(b)

if y < x:
    print(0)
else:
    print(y-x+1)
