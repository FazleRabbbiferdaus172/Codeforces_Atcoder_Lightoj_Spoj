n, x = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]

la = [0]*int(10e5+5)

ans = 0

for i in l:
    ans += la[i ^ x]
    la[i] += 1

print(ans)
