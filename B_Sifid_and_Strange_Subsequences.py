for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    lt0, ge0 = [], []

    for i in l:
        if i < 0:
            lt0 += [i]
        else:
            ge0 += [i]
    if len(lt0) > 0:
        mxl, mnl = max(lt0), min(lt0)
        xxx = sorted(l, reverse=True).index(mnl)
        xxx2 = sorted(l, reverse=True).index(mxl)
        lim = abs(mxl-mnl)
        print(lim)
        xn = 0
        ans = []
        for j, i in enumerate(l):
            if i in lt0 and not i in ans:
                ans += [i]
            elif i > mnl and abs(mnl -)
            elif i == 0:

        print("lim=", lim, " ans=", len(ans)+len(lt0))
