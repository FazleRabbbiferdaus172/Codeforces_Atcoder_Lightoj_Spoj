"""N = 1200+1
mark = [0]*N
prime = []

for i in range(3, N, 2):
    if not mark[i]:
        for j in range(3*i, N, i+i):
            mark[j] = 1
prime.append(2)
for i in range(3, N, 2):
    if not mark[i]:
        prime.append(i)
pcount = 0
allcount = 0
xxx = []
for i in range(1, 20):
    for j in range(1, 20):
        ooo = i**2+2*i*j+i+1
        xxx.append(ooo)
        if ooo in prime:
            print("X Y:", i, j, "H:", i**2+2*i*j+i+1, "Prime")
            pcount += 1
        else:
            print("X Y:", i, j, "H:", i**2+2*i*j+i+1, "Not Prime")
        allcount += 1

print(pcount, allcount)
lll = list(set(xxx))
print(sorted(lll))"""

n = int(input())

if n % 2 == 1 and n > 4:
    x = n//2 - 1
    print(1, x)
else:
    print("NO")
