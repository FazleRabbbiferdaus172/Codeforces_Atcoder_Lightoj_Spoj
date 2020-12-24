s = list(input())
s = [0] + s
m = int(input())

for _ in range(m):
    l, r, k = map(int, input().split())
    k = k % (r-l+1)
    s = s[:l] + s[r-k+1:r+1] + s[l:l+r-l+1-k] + s[r+1:]


s.remove(0)
print("".join(s))
