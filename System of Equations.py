n, m = [int(x) for x in input().split()]
c = 0
for i in range(int(n**.5)+1):
    if i+(n-i**2)**2 == m:
        c += 1
print(c)
