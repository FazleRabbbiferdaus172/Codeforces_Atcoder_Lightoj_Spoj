import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())

    a = input().strip()
    b = input().strip()

    have = [0]*27
    need = [0]*27

    for i in a:
        have[ord(i)-ord("a")] += 1

    for i in b:
        need[ord(i)-ord("a")] += 1

    bad = False

    for i in range(25):
        xx = have[i] - need[i]
        if xx < 0 or xx % k:
            bad = True
            break
        #have[i] = need[i]
        have[i+1] += xx

    if bad:
        print("No")
    else:
        print("Yes")
