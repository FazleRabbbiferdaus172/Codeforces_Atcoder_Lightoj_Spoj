n = int(input())

l = list(map(int, input().split()))

s = sum(l)
ans = 0

for i in range(1, 6):
    if (s+i) % (n+1) == 1:
        continue

    ans += 1

print(ans)
