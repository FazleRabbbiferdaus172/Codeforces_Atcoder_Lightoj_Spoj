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
        lim = abs(mxl-mnl)
        print(lim)
        xn = 0
        for i in ge0:
            if i <= lim:
                xn += 1
        print("lim=", lim, " ans=", xn+len(lt0))
