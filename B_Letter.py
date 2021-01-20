s1 = list(input())
s2 = input()
c = 0
for i in s2:
    if i == " ":
        c += 1
        continue

    if i in s1:
        c += 1
        s1.remove(i)

if c == len(s2):
    print("YES")
else:
    print("NO")
