n, m, k, t = map(int, input().split())

waste = []

for _ in range(k):
    i, j = map(int, input().split())
    waste += [(i-1)*m + (j-1)]
waste.sort()
put = ["Carrots", "Kiwis", "Grapes"]

for _ in range(t):
    i, j = map(int, input().split())
    numc = (i-1)*m + (j-1)
    c = 0
    for x in waste:
        #print(x, numc)
        if x > numc:
            break
        c += 1

    if numc in waste:
        print("Waste")
    else:
        print(put[(numc - c) % 3])
