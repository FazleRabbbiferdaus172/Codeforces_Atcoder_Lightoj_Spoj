n = int(input())

l = list(map(int, input().split()))
l.sort()

f_s, f_l = l.count(l[0]), l.count(l[-1])
ans = 0
if n == 2:
    ans = 0
elif f_s > 1 and f_l > 1:
    ans = l[-1] - l[0]
elif f_s == 1 and f_l == 1:
    if l[-1] - l[1] <= l[-2] - l[0]:
        ans = l[-1] - l[1]
    else:
        ans = l[-2] - l[0]
elif f_s == 1 and f_l > 1:
    ans = l[-1] - l[1]
elif f_l == 1 and f_s > 1:
    ans = l[-2] - l[0]

print(ans)
