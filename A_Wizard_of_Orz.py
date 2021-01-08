import math
for i in range(int(input())):
    n = int(input())
    num = "0123456789"
    ans = "989"
    one = n - 3
    if one > 0:
        adds = num*(one//10) + num[:(one % 10)]
        print(ans+adds)
    else:

        print(ans[:n])
