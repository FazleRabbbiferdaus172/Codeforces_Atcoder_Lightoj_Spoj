n = input()
chk = ['1', '4']
s = sorted(list(set(list(n))))
if s == chk and '444' not in n and n[0] != '4':
    print("YES")
elif n.count('1') == len(n):
    print("YES")
else:
    print("NO")
