max_a = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    max_a = max(max_a, a+b)

print(max_a)
