for _ in range(int(input())):
    s = list(input())
    x = ['a'] + s
    x = "".join(x)
    y = s + ['a']
    y = "".join(y)
    if x[::-1] != x:
        print("YES")
        print(x)
        #print("hey ", x, x[::-1])
    elif y[::-1] != y:
        print("YES")
        print(y)
        #print("hey ", y, y[::-1])
    else:
        print("NO")
