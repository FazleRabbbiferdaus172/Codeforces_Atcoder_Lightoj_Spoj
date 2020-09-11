a, b = input().split()

k = len(b)
a, b = int(a), int(b)
if k > a:
    print(-1)
else:
    if k == 1:
        print((b*(10**(a-1))))
    if k > 1:
        print((b*(10**(a-2))))
