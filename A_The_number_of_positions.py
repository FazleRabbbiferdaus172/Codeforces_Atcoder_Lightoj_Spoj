n, a, b = map(int, input().split())

c = 0
pos = a+1
# print(n-pos)
while pos <= n:
    # print(pos)
    if pos-1 >= a and (n-pos) <= b:
        c += 1
    pos += 1
print(c)
