s = list(input())

ans = ""
i = 0
while i < len(s):
    if s[i] == ".":
        ans += '0'
        i += 1
    elif s[i] == "-":
        if i+1 < len(s) and s[i+1] == ".":
            ans += '1'
        elif i+1 < len(s) and s[i+1] == "-":
            ans += '2'
        i += 2

print(ans)
