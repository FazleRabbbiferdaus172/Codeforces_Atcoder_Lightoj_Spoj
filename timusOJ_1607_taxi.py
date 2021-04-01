a, b, x, y = map(int, input().split())
if a > x:
    x = a

while a != x:
    a = min(a+b, x)
    x = max(a, x-y)
    #print(a, x)
print(a)
