import math
x = 1
while x:
    x = int(input())
    # print(x)
    if x == 0:
        break
    l = []
    for _ in range(x):
        l += [int(input().strip())]
    count = 0
    tot = 0
    for i in range(x):
        for j in range(i+1, x):
            tot += 1
            #print("tot", tot)
            if math.gcd(l[i], l[j]) == 1:
                #print("ok", l[i], l[j])
                count += 1

    if count == 0:
        print("No estimate for this data set.")
    else:
        # print(tot)
        ans = ((tot*6)/count)**.5
        print("{:.6f}".format(ans))
