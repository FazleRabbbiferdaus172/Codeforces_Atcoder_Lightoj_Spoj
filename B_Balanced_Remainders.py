for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = [0, 0, 0]
    for i in l:
        if i % 3 == 0:
            c[0] += 1
        elif i % 3 == 1:
            c[1] += 1
        else:
            c[2] += 1

    avg = sum(c)//3
    need = [avg-i for i in c]
    #print("need 1:", need)
    c = 0
    for i in range(2):
        if need[i] < 0:
            while need[i] < 0:
                need[i] += 1
                need[i+1] -= 1
                c += 1
    #print("need 2: ", need)
    need[0], need[1], need[2] = need[2], need[0], need[1]
    #print("changed", need)
    for i in range(2):
        if need[i] < 0:
            while need[i] < 0:
                need[i] += 1
                need[i+1] -= 1
                c += 1
    #print("need 3: ", need)
    print(c)
