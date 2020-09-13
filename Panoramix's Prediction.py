prime = [True] * 51
nprime = []
p = 2
prime[0], prime[1] = False, False

while(p * p <= 51):
    if prime[p]:

        for i in range(p*2, 51, p):
            prime[i] = False
    p += 1

for j, i in enumerate(prime):
    if i:
        nprime.append(j)

n, m = [int(x) for x in input().split()]
if prime[n] and prime[m]:
    if nprime.index(n) + 1 == nprime.index(m):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
