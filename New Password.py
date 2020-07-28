import string
l = list(string.ascii_lowercase)
n, k = [int(x) for x in input().split()]
ans = l[:k]*(n//k)
ans += ans[:n % k]

print(''.join(ans))
