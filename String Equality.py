for _ in range(int(input())):
    n, k = map(int, input().split())

    a = input()
    b = input()

    have = [0]*27
    need = [0]*27

    for i in a:
        have[ord(i)-ord("a")] += 1

    for i in b:
        need[ord(i)-ord("a")] += 1

    bad = False

    for i in range(26):
        if have[i] < need[i] or (have[i] - need[i]) % k != 0:
            bad = True
        have[i+1] += have[i]

    if bad:
        print("No")
    else:
        print("Yes")
