
i, j = 0, 0

for x in range(1, 6):
    l = list(input().split())
    if '1' in l:
        i, j = x, l.index('1')+1

print(abs(i-3)+abs(j-3))
