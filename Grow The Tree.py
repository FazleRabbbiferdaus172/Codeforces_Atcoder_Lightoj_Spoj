n = int(input())

l = list(map(int, input().split()))

l.sort(reverse=True)
k = n//2 + n % 2

x = sum(l[:k])
y = sum(l[k:])

print(x**2+y**2)
