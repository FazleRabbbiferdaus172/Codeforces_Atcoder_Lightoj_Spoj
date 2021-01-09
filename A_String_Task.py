s = input()
ans = ""
v = 'aeiouy'
for i in s:
    x = i.lower()
    if x not in v:
        ans += "."
        ans += x
print(ans)
