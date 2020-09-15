import math
for _ in range(int(input())):
    x, y, k = [int(x) for x in input().split()]
    mt = (y*k+k-1)//(x-1)+k+((y*k+k-1) % (x-1) > 0)
    # print((y*k+k-1))
    #print((y*k+k-1) // (x-1))
    #print((y*k+k-1) % (x-1))
    print(mt)
