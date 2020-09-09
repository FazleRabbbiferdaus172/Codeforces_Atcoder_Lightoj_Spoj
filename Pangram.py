n = int(input())
s = input().lower()
s = list(s)
s = set(s)

if len(s) == 26:
    print("YES")
else:
    print("NO")
