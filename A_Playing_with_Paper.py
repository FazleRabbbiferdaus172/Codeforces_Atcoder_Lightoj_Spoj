import math
a, b = map(int, input().split())
c = 0
while b != 0:
    c += a//b
    a, b = b, a % b

    #print(a, b)
'''
while a != b:
    a, b = (max(a, b) - min(a, b)), min(a, b)
    c += 1
    print(a, b)
'''

print(c)
