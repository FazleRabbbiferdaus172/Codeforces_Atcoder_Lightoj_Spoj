n = int(input())

res = 0

while n > 0:
    res += n % 2
    n //= 2

print(res)
