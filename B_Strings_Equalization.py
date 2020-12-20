for _ in range(int(input())):
    s = input()
    t = input()

    ans = "NO"
    for i in s:
        if i in t:
            ans = "YES"

            break

    print(ans)
