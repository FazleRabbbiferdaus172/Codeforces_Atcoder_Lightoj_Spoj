t = int(input())

for _ in range(t):
    n = int(input())
    if n <= 3:
        print(n-1)
    elif n % 2 == 0:
        print(2)
    elif n % 2 == 1:
        print(3)
