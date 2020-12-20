def is_fair(x):
    f = x
    flag = 1
    while f:
        g = f % 10

        if g == 0:
            g = 1

        if x % g != 0:
            flag = 0
            break

        f //= 10

    return flag


lcm_list = [2, 6, 12, 60, 420, 820, 2520]
for _ in range(int(input().strip())):
    n = int(input().strip())
    '''x = list(n)
    xx = list(set(x))
    xx = [int(i) for i in xx]
    if 0 in xx:
        xx.remove(0)
    lcm = 1
    for i in xx:
        lcm = compute_lcm(i, lcm)
    print("lcm", lcm)
    mm = int(n) // lcm
    ans = lcm
    if mm != 1:
        while lcm*mm < int(n):
            mm += 1
    print("mm", mm)
    ans = mm*lcm
    print(ans)'''

    while not is_fair(n):
        n += 1

    print(n)
