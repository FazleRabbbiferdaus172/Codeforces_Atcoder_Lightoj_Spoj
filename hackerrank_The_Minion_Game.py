def minion_game(string):
    # your code goes here
    stu, kvn = 0, 0
    vwl = "AEIOUaeiou"
    for i in range(len(string)):
        if string[i] not in vwl:
            # for j in range(i+1, len(string) +1):
                #stu += [string[i:j]]
            stu += len(string) - i
        else:
            # for j in range(i+1, len(string) +1):
                #stu += [string[i:j]]
            kvn += len(string) - i
    if stu > kvn:
        print("Stuart", stu)
    elif kvn > stu:
        print("Kevin", kvn)
    else:
        print("Draw")
    #print(stu, kvn)
