n = int(input())
f = 0
for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        print(x//2)
    elif f == 0:
        print(int(x//2)+1)
        f = 1
    else:
        print(int(x//2))
        f = 0
