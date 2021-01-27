for _ in range(int(input())):
    n = int(input())
    s = input()
    ss = ['E', 'S', 'W', 'N']
    ans = 0
    for i in s:
        if i == '0':
            ans += 1
        else:
            ans -= 1

        ans %= 4

    print(ss[ans])
