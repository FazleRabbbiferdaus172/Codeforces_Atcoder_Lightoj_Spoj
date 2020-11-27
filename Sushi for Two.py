n = int(input())
l = list(map(int, input().split()))
cou1 = 1
cou2 = 1
ans = 0
xx = 0
for i in range(n-1):
    if l[i] == l[i+1] and l[i] == 1:
        cou1 += 1
    elif l[i] == l[i+1] and l[i] == 2:
        cou2 += 1
    elif l[i] == 1 and l[i+1] == 2:
        xx = min(cou1, cou2)
        ans = max(xx, ans)
        cou2 = 1
    elif l[i] == 2 and l[i+1] == 1:
        xx = min(cou1, cou2)
        ans = max(xx, ans)
        cou1 = 1
    # print("l[i]: {} , l[i+1]: {} , cou1: {} , cou2: {} , xx: {} , ans: {} ".
    #      format(l[i], l[i+1], cou1, cou2, xx, ans*2))
xx = min(cou1, cou2)
ans = max(xx, ans)
print(ans*2)
