a, b = map(int, input().split())

ans = 0
ans += a
count = 1
while ans < b:
    ans -= 1
    ans += a
    count += 1
if b == 1:
    count = 0
print(count)
