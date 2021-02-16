for _ in range(int(input())):
    s = input()
    cur, mn, res = 0, 0, len(s)

    for i in range(len(s)):
        if s[i] == '+':
            cur += 1
        else:
            cur -= 1
        if cur < mn:
            mn = cur
            res += i + 1
        #print("res: ", res)

    print(res)
