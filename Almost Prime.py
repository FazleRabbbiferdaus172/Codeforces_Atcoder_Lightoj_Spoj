mark = [0]*(3000+1)
prime = []

for i in range(3, 3000+1, 2):
    if not mark[i]:
        for j in range(3*i, 3000+1, i+i):
            mark[j] = 1
prime.append(2)
for i in range(3, 3001, 2):
    if not mark[i]:
        prime.append(i)

# print(prime)
#vrfy = []
n = int(input())
ans = 0
for x in range(1, n+1):
    c = 0
    for i in prime:
        if(x % i == 0):
            c += 1
    if c == 2:
        ans += 1
        # vrfy.append(x)


print(ans)
# print(vrfy)
