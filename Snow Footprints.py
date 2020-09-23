n = int(input())
j = input()

if "RL" in j:
    i, ij = j.index('R'), j.index('RL')
    print(i+1, ij+1)
elif not "R" in j:
    if not "." in j:
        print(1, n)
    else:
        if ".L" in j and "L." in j:
            i, ij = j.index('.L'), j.index('L.')
            print(ij+1, i+1)
        elif ".L" in j and not "L." in j:
            i = j.index('.L')
            print(n, i+1)
        else:
            ij = j.index('L.')
            print(ij+1, 1)
elif not "L" in j:
    if not "." in j:
        print(1, n)
    else:
        if ".R" in j and "R." in j:
            i, ij = j.index('.R'), j.index('R.')
            print(i+2, ij+2)
        elif ".R" in j and not "R." in j:
            i = j.index('.R')
            print(i+2, n)
        else:
            ij = j.index('R.')
            print(1, ij+2)
