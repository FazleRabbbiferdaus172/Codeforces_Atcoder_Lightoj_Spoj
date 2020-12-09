a = list(input().strip())
b = list(input().strip())
ans = ""
# print(a)
for i in range(len(a)):
    ans += str(int(a[i]) ^ int(b[i]))
    # print(int(a[i]))

print(ans)
