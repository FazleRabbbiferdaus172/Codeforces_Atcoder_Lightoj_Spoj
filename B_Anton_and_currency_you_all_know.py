n = list(map(int, list(input())))
ans = -1
ind = -1
chk = n[-1]
for j, i in enumerate(n):
    if i % 2 == 0 and i < chk:
        ind = j
        break

if ind == -1:
    for i in range(len(n)-1, -1, -1):
        if n[i] % 2 == 0 and n[i] > chk:
            ind = i
            break

if ind != -1:
    n[-1], n[ind] = n[ind], n[-1]
    ans = list(map(str, n))
    ans = "".join(ans)

print(ans)
