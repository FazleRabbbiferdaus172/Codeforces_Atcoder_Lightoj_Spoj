n = int(input())
seg = []
mn, mx = float("inf"), -1
for _ in range(n):
    l, r = map(int, input().split())
    mn = min(l, mn)
    mx = max(r, mx)
    seg.append([l, r])

find = [mn, mx]
for i in range(n):
    if seg[i] == find:
        print(i+1)
        break
else:
    print(-1)
