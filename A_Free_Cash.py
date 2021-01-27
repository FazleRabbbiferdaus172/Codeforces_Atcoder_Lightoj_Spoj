n = int(input())

prev = [-1, -1]
c = 1
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    x = [a, b]
    if prev == x:
        c += 1
    else:
        prev[0], prev[1] = a, b
        ans = max(c, ans)
        c = 1
ans = max(c, ans)
print(ans)
