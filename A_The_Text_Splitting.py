import sys

n, p, q = map(int, input().split())
s = input()
for a in range(n+1):
    for b in range(n+1):
        if a*p + b*q == n:
            print(a+b)

            for i in range(a):
                print(s[i*p: i*p + p])

            s = s[a*p:]

            for i in range(b):
                print(s[i*q:i*q+q])

            sys.exit(0)

print(-1)
