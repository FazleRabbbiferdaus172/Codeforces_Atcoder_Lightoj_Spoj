n = int(input())
s = list(map(int, input().split()))
l = sorted(s, reverse=True)
ans = 0
c = 0
for i in l:
    #print(i*c + 1)
    ans += i*c + 1
    c += 1

print(ans)

for i in l:
    u = s.index(i)
    print(u+1, end=" ")
    s[u] = -1
print()
