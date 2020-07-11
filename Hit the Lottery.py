n = int(input())

l = [100, 20, 10, 5, 1]
nb, i = 0, 0
while n:
    nb += n // l[i]
    n %= l[i]
    i += 1
print(nb)
