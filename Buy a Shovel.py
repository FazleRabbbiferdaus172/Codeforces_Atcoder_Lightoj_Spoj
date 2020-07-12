s, c = [int(x) for x in input().split()]

i = 1
while True:
    if((i*s) % 10 == 0 or (i*s - c) % 10 == 0):
        break
    i += 1

print(i)
