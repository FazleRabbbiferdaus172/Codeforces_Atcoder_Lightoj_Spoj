
for t in range(int(input())):
    s = input()
    if s[0] == s[-1]:
        print("NO")
    else:
        count = 0
        x = s[0]
        b = ""
        for i in s:
            if i == x:
                count += 1
                b += '('
            else:
                b += ')'

        if len(s) - count != count:
            print("NO")
        else:
            stk = []
            for i in b:
                if i == '(':
                    stk += '('
                else:
                    stk.pop(0)
            if len(stk):
                print("NO")
                sys.exit(0)
            else:
                print("YES")
