n = int(input())
s = list(input())
q = int(input())
r = 0
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1 and not r:
        s[a-1], s[b-1] = s[b-1], s[a-1]
    elif t == 1 and r:
        if a <= n:
            a += n
        else:
            a -= n
        if b <= n:
            b += n
        else:
            b -= n
        s[a-1], s[b-1] = s[b-1], s[a-1]
    if t == 2:
        r ^= 1
if r:
    s = s[n:] + s[:n]
print("".join(s))
