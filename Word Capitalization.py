l = input()

s = l[0]

if ord(s) < ord('a'):
    print(l)
else:
    x = ord(s) - ord('a')
    xx = chr(ord('A') + x)
    ans = xx + l[1:]
    print(ans)
