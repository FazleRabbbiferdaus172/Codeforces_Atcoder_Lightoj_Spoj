import math
l = [2, 3, 4, 5, 6, 7, 8, 9, 10]

mul = 1
ans = 1
for i in l:
    ans = (ans*i)//math.gcd(ans, i)

n = int(input())

print(n//ans)
