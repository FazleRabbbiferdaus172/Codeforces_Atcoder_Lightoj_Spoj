n = int(input())

a = list(map(int, input().split()))
b = []

b = a.copy()
mp = dict()
b.sort()

for i in range(n):
    mp[b[i]] = i
# print(mp)
#print("before a", *a)
for i in range(n):
    a[i] = mp[a[i]]
#print("after a", *a)
L = -1
for i in range(n):
    if a[i] != i:
        #print("breaking", a[i], i)
        L = i
        break

R = -1
for i in range(n-1, -1, -1):
    if a[i] != i:
        R = i
        break

if L == -1 or R == -1:
    print("yes")
    print(1, 1)
else:
    ff = a[L:R+1]
    ff.reverse()
    chk = a[0:L] + ff + a[R+1:]
    if chk == sorted(a):
        print("yes")
        print(L+1, R+1)
    else:
        print("no")


# print(a)
# print(mp)
# print(*a)
# print(*b)
