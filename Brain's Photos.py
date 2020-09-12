n, m = [int(x) for x in input().split()]

inp = []

for i in range(n):
    inp.append(input().split())
color = "#Black&White"
for i in inp:
    if 'C' in i or 'M' in i or 'Y' in i:
        color = "#Color"
        break

print(color)
