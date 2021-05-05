for _ in range(int(input())):
    n = int(input())
    ans = 0
    ans = []
    for i in range(1, n+1):
        if len(set(list((str(i))))) == 1:
            ans += [i]
    print(len(ans))
