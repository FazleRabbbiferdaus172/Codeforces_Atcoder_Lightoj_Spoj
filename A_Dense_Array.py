for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(n-1):
        mn, mx, = min(l[i], l[i+1]), max(l[i], l[i+1])
        if mx/mn > 2:
            while mn < mx:
                mn *= 2
                #print("mn: ", mn, "mx: ", mx)
                c += 1
            c -= 1

    print(c)
