n = int(input())

ans = [n]

for i in range(1, n):
    ans += [i]


print(*ans)
