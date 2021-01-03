n, b, p = map(int, input().split())
ansb = 0
anst = n*p
while n > 1:
    x = n//2
    y = n % 2
    n -= x
    ansb += b*x*2 + x
print(ansb, anst)
