def subsets(s):
    if s == []:
        return [s]
    sets = [s]
    for i in range(0, len(s)):
        tmp_subsets = subsets(s[:i] + s[i+1:])
        for subset in tmp_subsets:
            if subset not in sets:
                sets.append(subset)
    return sets


l = list("123456789")
sset = subsets(l)
for _ in range(int(input())):
    n = int(input())
    m = int(1e6)

    i = int(n) - 1
    if n > 45:
        print(-1)
    elif n < 10:
        print(n)
    else:
        s = ""
        for i in range(9, 0, -1):
            if i <= n:
                n -= i
                s = str(i) + s

        print(s)
