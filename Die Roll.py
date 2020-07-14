from fractions import Fraction

a, b = [int(x) for x in input().split()]

c = 6 - max(a, b)+1

f = Fraction(c, 6)

if f == 1:
    print('1/1')
elif f == 0:
    print('0/0')
else:
    print(f)
