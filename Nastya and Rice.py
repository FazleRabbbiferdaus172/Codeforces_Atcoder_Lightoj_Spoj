for _ in range(int(input())):
    n, a, b, c, d = [int(x) for x in input().split()]

    t_a_min, t_a_max = (c-d)/n, (c+d)/n
    if (a+b) >= t_a_min and (a-b) <= t_a_max:
        print("YES")
    else:
        print("NO")
