n = int(input())
l = list(input())

i = 1
dv = []

while i*i <= n:
    if n % i == 0:
        dv.append(i)
        if i*i != n:
            dv.append(n//i)
    i += 1

dv.sort()

for i in dv:
    ans = ""
    a = l[0:i]
    a.reverse()
    #print("a", a)
    a = "".join(a)
    b = l[i:]
    b = "".join(b)
    #print("b", b)
    ans = a+b
    l = list(ans)

    # print(l)

print("".join(l))

# important thing to learn
'''l = list(l)
for i in reversed(dv):
    #l = l[0:i:-1] + l[i:]
    l = l[i-1::-1] + l[i:]
    print(l)'''
