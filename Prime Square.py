import math
number = int(1500)
primes = []
for i in range(2, number+1):
    primes.append(i)

i = 2
# from 2 to sqrt(number)
while(i <= int(math.sqrt(number))):
    # if i is in list
    # then we gotta delete its multiples
    if i in primes:
        # j will give multiples of i,
        # starting from 2*i
        for j in range(i*2, number+1, i):
            if j in primes:
                # deleting the multiple if found in list
                primes.remove(j)
    i = i+1

# print(primes)

for _ in range(int(input())):
    n = int(input())
    ans = []
    if n in primes:
        ans = [[1]*n for i in range(n)]
    else:
        k = n
        for i in primes:
            if i > n and not i-n+1 in primes:
                k = i-n+1
                break

        # print(k)
        ans = [[1]*n for i in range(n)]

        #k = k-n+1
        # print(k)
        for i in range(n):
            for j in range(n):
                if i == j:
                    ans[i][j] = k

    for i in ans:
        print(*i)
