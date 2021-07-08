n, q = map(int, input().split())
s = input()
pre = [0]*n
pre[0] = (ord(s[0]) - ord('a') + 1)
for i in range(1, n):
    pre[i] = pre[i-1] + (ord(s[i]) - ord('a') + 1)
pre = [0] + pre
# print(pre)
for i in range(q):
    i, j = map(int, input().split())
    print(pre[j]-pre[i-1])
