n = int(input())
l = list(map(int, input().split()))


max_l, le = 0, 0

for i in range(2*n):
    if l[i % n] == 1:
        le += 1
        max_l = max(max_l, le)
    else:
        le = 0

print(max_l)
