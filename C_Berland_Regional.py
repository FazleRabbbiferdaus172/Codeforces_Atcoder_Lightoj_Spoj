for i in range(int(input())):
    n = int(input())
    uni_l = list(map(int, input().split()))
    skill_l = list(map(int, input().split()))

    uni_d = {}

    for i in range(n):
        if uni_l[i] in uni_d:
            uni_d[uni_l[i]] += [skill_l[i]]
        else:
            uni_d[uni_l[i]] = [skill_l[i]]
    rate = [0] * n
    for i in uni_d:
        temp = 0
        uni_rate = []
        for xx, j in enumerate(sorted(uni_d[i], reverse=True)):
            temp += j
            uni_rate += [temp]
            rate[xx] += temp
    print(rate)
