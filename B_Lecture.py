n, m = map(int, input().split())
w_m = dict()
for i in range(m):
    a, b = map(str, input().split())
    if len(a) > len(b):
        w_m[a] = b
    else:
        w_m[a] = a

sen = input().split()
ans = ""
for j, i in enumerate(sen):
    ans += w_m[i]
    if j == n-1:
        continue
    ans += " "
print(ans)
