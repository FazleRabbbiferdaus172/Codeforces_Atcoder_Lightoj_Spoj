n = int(input())

l = [int(x) for x in input().split()]

print(1, 1)
print(l[0]*(-1))
l[0] = 0

if n-1 == 0:
    print(1, 1)
    print(0)

else:
    print(2, n)
    for i in range(1, n):
        x = l[i] % n
        print((n-1)*x, end=" ")
        l[i] += (n-1)*x
    print()

print(1, n)

for i in l:
    print(i*(-1), end=" ")

print()
