n = input()

l = list(n)


for i in range(len(l)):
    if 5 <= int(l[i]) <= 9:
        l[i] = str(9-int(l[i]))


if int(l[0]) == 0:
    l[0] = "9"

res = int("".join(l))

print(res)
