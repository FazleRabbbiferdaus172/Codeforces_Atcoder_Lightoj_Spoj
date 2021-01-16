n, a = map(int, input().split())

a -= 1
l = list(map(int, input().split()))

ans = l[a]

i, j = a-1, a+1

while i >= 0 and j < n:
    if l[i] == 1 and l[j] == 1:
        ans += l[i] + l[j]
    i -= 1
    j += 1
while i >= 0:
    ans += l[i]
    i -= 1
while j < n:
    ans += l[j]
    j += 1
print(ans)
