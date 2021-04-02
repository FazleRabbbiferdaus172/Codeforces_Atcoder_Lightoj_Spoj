def ncr(n, m):
    '''
    ****Do not foget to intial 'da' everytime if there are multiple test cases*****
    based on formula: n C r + n C (r-1) = (n+1) C r then (n - 1) C r + (n - 1) C (r - 1) = n C r
    '''
    global da
    if m == 1:
        ans = n
    elif n == m or m == 0:
        ans = 1
    elif da[n-1][m] != -1 and da[n-1][m-1] != -1:
        ans = da[n-1][m] + da[n-1][m-1]
    else:
        ans = ncr(n-1, m) + ncr(n-1, m-1)
        da[n][m] = ans
    return ans


while True:
    n, m = map(int, input().split())

    if not n and not m:
        break
    da = [[-1]*100 for i in range(100+1)]
    ans = ncr(n, m)
    print("{} things taken {} at a time is {} exactly.".format(n, m, ans))
