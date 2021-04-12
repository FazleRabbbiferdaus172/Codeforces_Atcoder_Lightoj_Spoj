for _ in range(int(input())):
    n, k = map(int, input().split())

    if n % 2 == 1 and k > n // 2:
        print(-1)
        continue
    elif n % 2 == 0 and k > (n // 2) - 1:
        print(-1)
        continue
    ans = [-1, 1]
    rem = [i for i in range(3, 2*k+2, 2)]
    for i in range(2, 2*k+2):
        # print(i)
        if i % 2 == 0 and k > 0:
            ans.append(rem[0])
            rem.remove(ans[i])
        else:
            ans.append(i-1)
    for i in range(2*k+2, n+1):
        ans.append(i)
    print(*ans[1:])
