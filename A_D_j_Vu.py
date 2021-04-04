for _ in range(int(input())):
    s = list(input())
    x = ['a'] + s
    y = s + ['a']
    if x.reverse() != x:
        print("YES")
        print("".join(x))
    elif y.reverse() != y:
        print("YES")
        print("".join(y))
    else:
        print("NO")
