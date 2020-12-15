n = input()

l = list(map(int, input().split()))
c5 = l.count(5)
c0 = l.count(0)
if c5 >= 9 and c0 >= 1:
    while c5*5 % 9 != 0:
        c5 -= 1
    a5 = ['5']*c5 + ['0']*c0
    print("".join(a5))
elif c0 == 0:
    print(-1)
else:
    print(0)
