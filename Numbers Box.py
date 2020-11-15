for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    l = []

    for i in range(n):
        l.append([int(x) for x in input().split()])
    nege = []
    pose = []
    for i in l:
        for j in i:
            if j < 0:
                nege.append(-1*j)
            else:
                pose.append(j)
    print(nege, pose)

    if len(nege) % 2 == 0:
        print(sum(pose) + sum(nege))
    else:
        print(sum(pose) + sum(nege)-2*min(min(nege), min(pose)))
