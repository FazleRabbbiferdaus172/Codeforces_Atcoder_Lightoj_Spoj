a = input()
b = input()
c = input()

ans = "YES"

x = a + b
x = list(x)
c = list(c)
x.sort()
c.sort()

if x != c:
    ans = "NO"

print(ans)
