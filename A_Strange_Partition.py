import math
for _ in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    n_l = [math.ceil(i/x) for i in l]
    mx = sum(n_l)
    mn = math.ceil(sum(l)/x)
    print(mn, mx)
