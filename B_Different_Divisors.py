def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    prime_nums = []
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            prime_nums.append(p)

    return prime_nums


prime = SieveOfEratosthenes(int(1e5)+7)

for _ in range(int(input())):
    d = int(input())
    p, q = 1, 1
    for i in prime:
        if i >= d+1:
            p = i
            break
    for i in prime:
        if i >= d+p:
            q = i
            break
    #print(p, q)
    print(min(p**3, p*q))
