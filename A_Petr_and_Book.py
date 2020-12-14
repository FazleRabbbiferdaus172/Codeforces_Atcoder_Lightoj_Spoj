n = int(input())

l = list(map(int, input().split()))
i = 0
while n > 0:
    n -= l[i]
    i += 1
    i %= 7

if i == 0:
    i = 7
print(i)
