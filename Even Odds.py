import math
a, b = [int(x) for x in input().split()]

d = math.ceil(a/2)

if b > d:
    print(2*(b-d))
else:
    print(2*b-1)
