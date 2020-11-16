for _ in range(int(input())):
    s = input()

    j = min(s.count('1'), s.count('0'))

    if j % 2 == 1:
        print("DA")
    else:
        print("NET")
