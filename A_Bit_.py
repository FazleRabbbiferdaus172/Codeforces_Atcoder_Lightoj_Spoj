ans = 0
n = int(input())
a, b = ['+', '+', 'X'], ['-', '-', 'X']
a.sort()
b.sort()
#a = "".join(a)
#b = "".join(b)
for _ in range(n):
    s = sorted(list(input()))
    #s = "".join(s)
    #print(s, a)

    if s == a:
        ans += 1
    elif s == b:
        ans -= 1
print(ans)
