n, a, b, c = map(int, input().split())
mx = -1
for i in range(0, (n//a)+1):
    for j in range(0, (n//b)+1):
        k = (n - i*a - j*b)//c
        #print(i, j, k)
        if (a*i + b*j + c*k) == n and k >= 0:
            mx = max(mx, i+j+k)
            # if mx > n:
            #print(i, j, k)


print(mx)
