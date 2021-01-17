t, sx, sy, ex, ey = map(int, input().split())

s = input() + "$"
ans = -1
for j, i in enumerate(s):
    if sx < ex and i == 'E':
        sx += 1
    elif sx > ex and i == 'W':
        sx -= 1

    if sy < ey and i == "N":
        sy += 1
    elif sy > ey and i == "S":
        sy -= 1
    if sx == ex and sy == ey:
        ans = j + 1
        break
print(ans)
