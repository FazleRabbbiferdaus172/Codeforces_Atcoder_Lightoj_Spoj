l = list(input())
l = l[1:-1]
l = set(l)
if ' ' in l and ',' in l:
    print(len(l)-2)
else:
    print(len(l))
