n = input()
zc = 0
i = len(n) - 1
while i >= 0:
    if n[i] == '0':
        zc += 1
    else:
        break
    i -= 1

x = '0'*zc + n

if x == x[::-1]:
    print("Yes")
else:
    print("No")
