import math
for i in range(int(input())):
    n = int(input())
    temp = math.floor(math.log2(n))
    print(2**temp - 1)
