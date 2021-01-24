n = int(input())
l = list(map(int, input().split()))
sl = sorted(l)
sml, srl = [0]*n, [0]*n
sml[0] = l[0]
srl[0] = sl[0]
for i in range(1, n):
    sml[i] = sml[i-1] + l[i]
    srl[i] = srl[i-1] + sl[i]
sml += [0]
srl += [0]
q = int(input())

for _ in range(q):
    t, l, r = map(int, input().split())
    l, r = l-1, r-1
    if t == 1:
        print(sml[r]-sml[l-1])
    else:
        print(srl[r] - srl[l-1])
