

s = input()
n = len(s)
ansi, ansj = -1, -1
found = False
for i in range(n-1):
    if s[i] == s[i+1]:
        ansi, ansj = i+1, i+2
        found = True
        break
if found:
    print(ansi, ansj)
else:
    for i in range(n-2):
        if s[i] == s[i+2]:
            ansi, ansj = i+1, i+3
            break

    print(ansi, ansj)
