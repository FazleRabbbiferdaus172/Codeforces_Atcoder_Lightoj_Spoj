n = input()
a = list(map(int, input().split()))
m = input()
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
gear = []

for i in a:
    for j in b:
        if j/i == j//i:
            gear += [j//i]
ans = gear.count(max(gear))
print(ans)
