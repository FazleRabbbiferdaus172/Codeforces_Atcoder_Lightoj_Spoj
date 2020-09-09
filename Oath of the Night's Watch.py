n = int(input())

l = [int(x) for x in input().split()]
if len(l) <= 2:
    print(0)
else:
    mx, mn = max(l), min(l)
    if mx == mn:
        print(0)
    else:
        cnt_feed = l.count(mx)+l.count(mn)

        print(n-cnt_feed)
