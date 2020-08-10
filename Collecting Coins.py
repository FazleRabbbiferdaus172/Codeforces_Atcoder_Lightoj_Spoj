t = int(input())

for i in range(t):
    a, b, c, n = [int(x) for x in input().split()]

    m = max(a, b, c)

    n -= (m-a)+(m-b)+(m-c)
    if(n % 3 == 0 and n >= 0):
        print("YES")
    else:
        print("No")
