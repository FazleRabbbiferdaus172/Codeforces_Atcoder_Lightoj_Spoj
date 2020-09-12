import math
n, m, a = [int(x) for x in input().split()]

print(math.ceil(n/a) * math.ceil(m/a))
