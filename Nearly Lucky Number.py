xx = list(input())
ans = "NO"
n = xx.count('4') + xx.count('7')
n = list(str(n))
# print(n)

if n.count('4') + n.count('7') == len(n):
    ans = "YES"

print(ans)
