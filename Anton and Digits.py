l = list(map(int, input().split()))

x = min(l[0], l[2], l[3])

y = min((l[0]-x), l[1])

print(x*256+y*32)
