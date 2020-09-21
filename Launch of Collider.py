n = int(input())
s = input()
l = [int(x) for x in input().split()]

t = float('inf')

for i in range(1, n):
    if s[i-1] == 'R' and s[i] == 'L':
        x = (l[i]-l[i-1])//2
        t = min(x, t)

if t == float('inf'):
    print(-1)
else:
    print(t)
