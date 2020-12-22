def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    prime_nums = []
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    return prime


prime = SieveOfEratosthenes(int(1e6)+7)
# print(prime)
n = int(input())
l = list(map(int, input().split()))
for i in l:
    if int(i**0.5) == i**0.5 and prime[int(i**0.5)]:
        print("YES")
    else:
        print("NO")
