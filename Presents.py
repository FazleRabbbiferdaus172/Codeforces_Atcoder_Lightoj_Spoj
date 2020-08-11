n = int(input())

d = dict()

l = [int(x) for x in input().split()]
ans = [0]*n

for i in range(n):
    ans[l[i]-1] = i+1

print(*ans)
