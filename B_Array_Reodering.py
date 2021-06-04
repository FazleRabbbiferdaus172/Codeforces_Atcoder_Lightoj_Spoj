def divisor(n):
    i = 1
    dv = []
    while i*i <= n:
        if n % i == 0:
            dv.append(i)
            if i*i != n:
                dv.append(n//i)
        i += 1
    dv.remove(1)
    return dv


def SieveOfEratosthenes(n):
    global d, l
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
                if i in l and p in l and p != 2:
                    d[i] = l.count(p)
        p += 1
    return prime


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    even, odd = [i for i in l if i % 2 == 0], sorted(
        [i for i in l if i % 2 == 1], reverse=True)
    ans = 0
    prime = SieveOfEratosthenes(100001)
    even_len = len(even)
    for i in range(even_len):
        ans += even_len - 1 - i + len(odd)

    for x, i in enumerate(odd):
        if not prime[i]:
            ans += d[i] + odd[x+1:].count(i)
        else:
            if i != 1:
                ans += odd[x+1:].count(i)

    print(ans)
