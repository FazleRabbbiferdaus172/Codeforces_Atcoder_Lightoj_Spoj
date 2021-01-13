s = input()

hello = [True, 'h', 'e', 'l', 'l', 'o']
x = 1
for i in s:
    if i == hello[x] and hello[x-1] == True:
        hello[x] = True
        x += 1
    if x > 5:
        break

if hello.count(True) == 6:
    print("YES")
else:
    print("NO")
