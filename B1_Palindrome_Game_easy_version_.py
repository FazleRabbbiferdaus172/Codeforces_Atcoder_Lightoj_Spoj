for i in range(int(input())):
    n = int(input())
    x = list(input())
    temp = x.copy()
    temp[n//2] = '1'
    # print(x)
    if x.count('0') % 2 == 0 and x.count('0') > 2:
        print("DRAW")
    elif x.count('0') > 2 and x[n//2] == '0' and temp == temp[::-1]:
        print("ALICE")
    else:
        print("BOB")
