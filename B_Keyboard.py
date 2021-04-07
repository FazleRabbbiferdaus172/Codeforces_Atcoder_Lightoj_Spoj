n, m, x = map(int, input().split())
g = []
isS = []
d = {}
for _ in range(n):
    z = input()
    g.append(z)
    if 'S' in z:
        isS = True

q = input()
s = input()
