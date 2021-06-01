def merge_the_tools(string, k):
    # your code goes here
    t = []
    j = 0
    for i in range(k, len(string)+1, k):
        t.append(string[j:i])
        j = i
    # print(t)
    u = []
    for i in t:
        d = {}
        temp = ""
        for j in i:
            if not j in d:
                d[j] = 1
                temp += j
        u += [temp]
    print(*u, sep="\n")
