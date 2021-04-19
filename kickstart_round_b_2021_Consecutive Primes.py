def SieveOfEratosthenes(n):
    global mark
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            mark.append(p)


mark = []

SieveOfEratosthenes(1000000)
print(mark[-1]*mark[-2])
for t in range(int(input())):
    z = int(input())
    ans = z
    for i in range(1, len(mark) - 1):
        # print(i)
        if mark[i]*mark[i-1] == z:
            # print("yes")
            ans = z
            break
        elif mark[i]*mark[i-1] > z:
            #print(mark[i], mark[i-1])
            break
        ans = mark[i]*mark[i-1]
    print("Case #{}:".format(t+1), ans)
    #print("ans_x", ans_x)
    # print(*adif)
