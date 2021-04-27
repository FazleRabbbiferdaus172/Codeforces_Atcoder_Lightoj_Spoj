import math
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    aa, bb, cc = int(10**(a-1)), int(10**(b-1)), int(10**(c-1))
    if c == min(a, b):
        print(aa, bb)
    else:
        bb += cc
        print(aa, bb)
    #print("gcd", math.gcd(aa, bb))
