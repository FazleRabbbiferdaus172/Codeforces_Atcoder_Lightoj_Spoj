import math
for _ in range(int(input())):
    n, x = [int(x) for x in input().split()]

    if n == 1 or n == 2:
        print(1)
    else:
        a = n - 2
        print(math.ceil(a/x)+1)
