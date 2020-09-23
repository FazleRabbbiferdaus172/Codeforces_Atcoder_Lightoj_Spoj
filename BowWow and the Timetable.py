import math
m = input()
n = int(m, 2)

if n == 0:
    print(0)
else:
    x = list(m).count('1')
    res = int(math.log(n, 4))
    if res == math.log(n, 4) and (x == 1 or x == len(m)):
        print(res)
    else:
        print(res+1)
