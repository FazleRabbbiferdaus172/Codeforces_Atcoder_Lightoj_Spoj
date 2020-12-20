import math

n = int(input())
if n % 2 == 0:
    print((n//2 + 1)*(n//2+1))
else:
    x = math.ceil(n/2)
    print(x*(x+1)*2)
