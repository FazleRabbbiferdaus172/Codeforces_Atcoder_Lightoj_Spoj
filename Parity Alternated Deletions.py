n = input()
l = list(map(int, input().split()))
l.sort(reverse=True)
odd, even = [], []

for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

e_l, o_l = len(even), len(odd)
most = min(e_l, o_l)
if n == 1:
    ans = 0
elif most == 0:
    ans = sum(l[1:])
elif e_l == most:
    ans = sum(odd[most+1:])
elif o_l == most:
    ans = sum(even[most+1:])

print(ans)
