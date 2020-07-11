d = dict()
for i in range(97, 123):
    d[chr(i)] = abs(97-i)+1

n = list(input())
a = d['a']
r = 0
for i in n:
    b = d[i]
    r += min(abs(b-a), 26-abs(b-a))
    a = b
print(r)
