n = input()
r = input()

l = n.split("|")
min_l = min(len(l[0]), len(l[1]))
max_l = max(len(l[0]), len(l[1]))

if len(l[0]) == len(l[1]) + len(r):
    print(n+r)
elif len(l[0]) + len(r) == len(l[1]):
    print(r+n)
elif min_l == max_l and len(r) % 2 == 2:
    d = len(r) // 2
    print(r[:d]+n+r[d:])
elif min_l + (max_l-min_l) == max_l and len(r) > (max_l-min_l):
    if (len(r)-(max_l-min_l)) % 2 == 0:
        d = (len(r)-(max_l-min_l)) // 2
        if max_l == len(l[0]):
            print(r[:d]+l[0]+"|"+l[1]+r[d:])
        else:
            print(r[d:]+l[0]+"|"+l[1]+r[:d])
    else:
        print("Impossible")
else:
    print("Impossible")
