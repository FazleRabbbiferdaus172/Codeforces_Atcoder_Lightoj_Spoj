s = input()
sa = []
if len(s) == 1:
    print(s)
else:
    s = list(s.split('+'))
    s.sort()
    for i in s:
        sa.append(i)
        sa.append('+')
    sa.pop(-1)
    for i in sa:
        print(i, end='')
