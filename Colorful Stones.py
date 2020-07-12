c = input()
s = input()
j, r, x = 1, 0, 2
if s[0] != c[0]:
    j, x = 0, 1
for i in s:
    if i == c[j]:
        r += 1
        j += 1
print(min(r+x, len(c)))
