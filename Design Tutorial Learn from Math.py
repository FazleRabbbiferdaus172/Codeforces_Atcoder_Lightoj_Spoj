N = int(10e6)+2
mark = [0]*N
prime = []

for i in range(3, N+1, 2):
    if not mark[i]:
        for j in range(3*i, N+1, i+i):
            mark[j] = 1
prime.append(2)
for i in range(3, N, 2):
    if not mark[i]:
        prime.append(i)

n = int(input())

a, b = 4, n-4

while a in prime or b in prime:
    a += 1
    b = n - a

print(a, b)
