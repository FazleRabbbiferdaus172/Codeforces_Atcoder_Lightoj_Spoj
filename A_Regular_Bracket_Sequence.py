for _ in range(int(input())):
    n = input()
    if len(n) % 2 == 1:
        print('No')
    elif n[0] == ')' or n[-1] == '(':
        print("No")
    else:
        print("Yes")
