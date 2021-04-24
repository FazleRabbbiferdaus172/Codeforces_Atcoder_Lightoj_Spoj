n = int(input())
s = list(input())
q = int(input())
r = 0
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1 and r % 2 == 0:
        s[a-1], s[b-1] = s[b-1], s[a-1]
    elif t == 1 and r % 2 == 1:
        s[b-1], s[a-1] = s[a-1], s[b-1]
    if t == 2:
        r += 1
print("".join(s))
