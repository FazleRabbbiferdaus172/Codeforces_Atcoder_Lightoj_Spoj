for _ in range(int(input())):
    n = int(input())
    x = str(n)[0]
    #temp = 0
    # if n < 10:
    #    temp += n % 10
    ans = 0
    #n //= 10
    #x = 10
    count = 0
    temp = n
    while n:
        #print("YO", n % x)
        ans += 9
        if n//10 == 0:
            ans -= 9
            ans += n % 10
            #print("yp1", n, n % 10, ans)
            if count > 0:
                ans -= 1
        #print("yp", ans)
        count += 1
        n //= 10
    if temp >= int(x*count) and count > 1:
        ans += 1
    print(ans)
    #print(x, "xxx", count)
