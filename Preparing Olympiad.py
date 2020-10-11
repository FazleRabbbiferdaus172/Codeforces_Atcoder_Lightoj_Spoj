n, l, r, x = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

# a.sort()

mask = (1 << n) - 1

ans = 0

for sub in range(mask+1):
    s, num = 0, 0
    hard, easy = float('-inf'), float('inf')
    for i in range(n):
        if (sub & (1 << i)) > 0:
            s += a[i]
            num += 1
            hard = max(a[i], hard)
            easy = min(a[i], easy)

    if s >= l and s <= r and hard - easy >= x and num >= 2:
        ans += 1

print(ans)
