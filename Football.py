n = int(input())
l = []
for _ in range(n):
    l.append(input())

s = set(l)
win = l[0]
goal = l.count(l[0])
for i in s:
    if l.count(i) > goal:
        win = i
        goal = l.count(i)

print(win)
