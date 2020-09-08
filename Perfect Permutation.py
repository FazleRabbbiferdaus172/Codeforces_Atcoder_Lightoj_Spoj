n = int(input())

if n % 2 == 1:
    print("-1")
else:
    i = 2
    j = 1
    l = []
    for _ in range(n//2):
        l.append(i)
        l.append(j)
        i += 2
        j += 2
    print(*l)
