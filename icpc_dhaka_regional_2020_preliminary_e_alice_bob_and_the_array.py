for t in range(1, int(input().strip()) + 1):
    n = int(input().strip())
    l = list(map(int, input().split()))
    xxx = max(l)
    x = sum([i for i in l if i >= 0])
    l = [i for i in l if i != 0]
    n = len(l)
    i = 0
    while i < n and l[i] <= 0:
        i += 1
    j = len(l) - 1
    while j >= 0 and l[j] <= 0:
        j -= 1
    c = 0

    for xx in range(i+1, j):
        if l[xx] < 0 and l[xx+1] > 0:
            c += 1
    if xxx < 0:
        x = xxx
    print("Case {}: {} {}".format(t, x, c))
