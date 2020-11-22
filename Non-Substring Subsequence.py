t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input()
    while q:
        l, r = map(int, input().split())
        sub = s[l-1:r]

        if sub[0] in s[0:l-1] or sub[-1] in s[r:]:
            print("YES")
        else:
            print("NO")
        q -= 1
