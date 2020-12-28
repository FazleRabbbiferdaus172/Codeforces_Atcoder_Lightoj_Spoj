import sys
x = input()
y = input()
l = len(x)
if len(x) > len(y):
    add = len(x) - len(y)
    add_z = "0"*add
    y = add_z + y
elif len(x) < len(y):
    add = len(y) - len(x)
    add_z = "0"*add
    x = add_z + x
    l = len(y)

for i in range(l):
    if int(x[i]) > int(y[i]):
        print(">")
        sys.exit(0)
    if int(x[i]) < int(y[i]):
        print("<")
        sys.exit(0)
print("=")
