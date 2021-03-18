for t in range(int(input())):
    s = input()
    if s[0] == s[-1]:
        print("NO")
    else:
        countx, county = 0, 0
        x = s[0]
        y = s[-1]
        b = ""
        for i in s:
            if i == x:
                countx += 1
                b += '('
            else:
                b += ')'
        c = ""
        for i in s:
            if i == y:
                county += 1
                b += ')'
            else:
                b += '('
        if countx != len(s)//2 and county != len(s)//2:
            print("NO")
        else:
            stk1, ex1 = chk(b)
            stk2, ex2 = chk(c)
            if ex1 and ex2:
                print("NO")
            elif len(stk1) and len(stk2):
                print("NO")
            else:
                print("YES")
