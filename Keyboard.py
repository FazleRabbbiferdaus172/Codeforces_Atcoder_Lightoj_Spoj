u_keybord = "qwertyuiop"
m_keybord = "asdfghjkl;"
l_keybord = "zxcvbnm,./"


def s(k, shift, a):
    if shift == 'R':
        if k.find(a) == 0:
            return a
        else:
            return k[k.find(a)-1]
    if shift == 'L':
        if k.find(a) == len(k)-1:
            return a
        else:
            return k[k.find(a)+1]


shift = input()
msg = input()
result = ""
for i in msg:
    if i in u_keybord:
        result += s(u_keybord, shift, i)
    elif i in m_keybord:
        result += s(m_keybord, shift, i)
    else:
        result += s(l_keybord, shift, i)

print(result)
