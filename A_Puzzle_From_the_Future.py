for _ in range(int(input())):
    n = int(input())
    l = map(int, list(input()))

    r = [-1]
    ans = []
    for i in l:
        if r[-1] != i+1:
            ans += ["1"]
            r += [i+1]
        else:
            ans += ["0"]
            r += [i]

    print("".join(ans))
