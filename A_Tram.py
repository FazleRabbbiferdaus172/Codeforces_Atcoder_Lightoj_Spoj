n = int(input())
mx = -1
x = 0
for i in range(n):
    a, b = map(int, input().split())
    x = x + b - a
    mx = max(x, mx)

print(mx)
