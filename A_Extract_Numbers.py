s = input()
s = s + ","
a = ""
b = ""
start, end = 0, 0
for i in range(len(s)):
    if s[i] == ';' or s[i] == ",":
        if start != end:
            f = s[start:end]
        else:
            f = ""
        # print(f)
        if f.isdigit() and f[0] != '0':
            a += f + ","
        else:
            if f == '0':
                a += f + ","
            else:
                b += f + ","

        start = end+1
        end += 1
    else:
        end += 1
if not a:
    a = "-"
else:
    a = a[:len(a)-1]
    a = '"' + a + '"'
if not b:
    b = "-"
else:
    b = b[:len(b)-1]
    b = '"' + b + '"'

print(a)
print(b)
