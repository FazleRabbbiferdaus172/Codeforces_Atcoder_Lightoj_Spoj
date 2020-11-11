
MOD = 7901
fact = [0]*1001
fact[0] = 1

for i in range(1, 1001):
    fact[i] = (fact[i-1]*i) % MOD


for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    d = dict()

    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = 1
    for i in d:
        ans = (ans * fact[d[i]]) % MOD
    # print(d)
    print(ans)
