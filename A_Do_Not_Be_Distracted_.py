for _ in range(int(input())):
    n = input()
    l = input()
    d = [l[0]]
    prev = l[0]
    ans = "YES"
    for i in l[1:]:
        if i == prev:
            continue
        else:
            if i in d:
                ans = "NO"
                break
            else:
                d += [i]
        prev = i
    print(ans)
