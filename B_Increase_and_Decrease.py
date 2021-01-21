n = int(input())

l = list(map(int, input().split()))

if sum(l) % n == 0:
    print(n)
else:
    print(n-1)
