s = input()
t = input()
xx = reversed(list(s))
xx = "".join(xx)
if xx == t:
    print("YES")
else:
    print("NO")
