n = int(input())
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

x = 0
c = 0
while n > 3:
    a, b = prime[x], n-prime[x]
    if b in prime:
        #print(a, b)
        n = b - a
        c += 1
        x = 0
    else:
        x += 1

print(c)
