n = int(input())
l = list(map(int, input().split()))

f, z = l.count(5), l.count(0)

if z == 0:
    ans = -1
else:
    ans = int('5'*((f//9)*9) + '0'*(z))

print(ans)
