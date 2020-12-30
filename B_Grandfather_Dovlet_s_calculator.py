a, b = map(int, input().split())

d = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
     '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

ans = 0
for i in range(a, b+1):
    s = str(i)
    for j in s:
        ans += d[j]
        #print(ans, j)

print(ans)
