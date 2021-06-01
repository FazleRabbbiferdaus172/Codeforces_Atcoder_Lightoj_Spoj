n, m = map(int, input().split())
l = []
for i in range(1, n//2+1):
    temp = ".|."*(2*(i-1)+1)
    xx = len(temp)
    temp = "-"*((m-xx)//2) + temp + "-"*((m-xx)//2)
    l += [temp]
temp = "-"*((m-7)//2)+"WELCOME"+"-"*((m-7)//2)

print("\n".join(l))
print(temp)
print("\n".join(reversed(l)))
