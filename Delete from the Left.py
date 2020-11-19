s = list(input())
t = list(input())
i, j = len(s)-1, len(t)-1
cc = 0
while i >= 0 and j >= 0 and s[i] == t[j]:
    cc += 1
    i -= 1
    j -= 1

print(len(s) + len(t) - 2*cc)
