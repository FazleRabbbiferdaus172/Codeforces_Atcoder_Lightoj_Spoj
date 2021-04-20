s = input()

sm = 0

for i in s:
    sm += int(i)

if sm % 9 == 0:
    print("Yes")
else:
    print("No")
