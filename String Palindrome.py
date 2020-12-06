n = input()
l = len(n)

i, j = 0, l//2
xx = n[i:j]
xy = xx[::-1]
ans = True

if n != n[::-1]:
    ans = False
if xx != xy:
    ans = False


if ans:
    print("Yes")
else:
    print("No")
