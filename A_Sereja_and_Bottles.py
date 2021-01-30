n = int(input())
s1, s2 = [], []
for i in range(n):
    a, b = map(int, input().split())
    s1 += [a]
    s2 += [b]
c = 0
for i in range(n):
    for j in range(n):

        if s1[i] == s2[j] and i != j:
            c += 1
            break

print(n - c)
