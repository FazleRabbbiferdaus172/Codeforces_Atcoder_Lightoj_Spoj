n = input()
l = list(map(int, input().split()))

i = l.index(max(l))
l.reverse()
j = len(l) - 1 - l.index(min(l))
ans = i + len(l) - j - 1
if i > j:
    ans -= 1
print(ans)
