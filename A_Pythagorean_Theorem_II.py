import math
n = int(input())
count = 0
for i in range(1, n):
    for j in range(i+1, n):
        #print(i, j)
        c = i*i + j*j
        if c > n*n:
            break
        if math.sqrt(c) == int(math.sqrt(c)):
            count += 1
print(count)
