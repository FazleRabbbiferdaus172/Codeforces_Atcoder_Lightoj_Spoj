for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    l = []
    c = 0
    for i in range(n):
        l.append([int(x) for x in input().split()])
    alln = []
    for i in l:
        for j in i:
            if j < 0:
                c += 1
            alln.append(abs(j))
    #print(nege, pose)

    if c % 2 == 0:
        print(sum(alln))
    else:
        print(sum(alln) - 2*min(alln))
