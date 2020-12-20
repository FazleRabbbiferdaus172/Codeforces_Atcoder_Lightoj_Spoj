import math
n, m = map(int, input().split())
bigt = n - (m-1)
mx = (bigt*(bigt-1))//2
share = n//m
rem = n % m
comb = share + 1
mn = ((comb*(comb-1))//2)*rem + ((share*(share-1))//2)*(m-rem)
print(mn, mx)
