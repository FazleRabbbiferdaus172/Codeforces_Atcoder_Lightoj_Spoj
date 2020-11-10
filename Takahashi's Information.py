r1 = [int(x) for x in input().split()]
r2 = [int(x) for x in input().split()]
r3 = [int(x) for x in input().split()]

for i in range(2):
    if r1[i] - r2[i] == r1[i+1] - r2[i+1] and r1[i] - r3[i] == r1[i+1] - r3[i+1] and r3[i] - r2[i] == r3[i+1] - r2[i+1]:
        isit = True
    else:
        isit = False
        break
if isit:
    print("Yes")
else:
    print("No")
