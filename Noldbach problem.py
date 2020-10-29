n, k = [int(x) for x in input().split()]
N = n+1
mark = [0]*N
prime = []

for i in range(3, N, 2):
    if not mark[i]:
        for j in range(3*i, N, i+i):
            mark[j] = 1
prime.append(2)
for i in range(3, N, 2):
    if not mark[i]:
        prime.append(i)

# print(prime)
c = 0
for j in prime:
    for i in range(1, len(prime)):
        #print(prime[i-1]+prime[i]+1, j)
        if prime[i-1]+prime[i]+1 == j:
            c += 1
            break

if c >= k:
    print("YES")
else:
    print("NO")
