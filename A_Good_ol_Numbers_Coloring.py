import math
for _ in range(int(input())):
    a, b = map(int, input().split())
    x = math.gcd(a, b)
    print("Finite" if x == 1 else "Infinite")
