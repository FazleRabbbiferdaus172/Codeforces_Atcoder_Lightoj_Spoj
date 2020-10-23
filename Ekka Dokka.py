
for t in range(1, int(input())+1):
    n = int(input())
    if n % 2 != 0:
        print("Case {}: Impossible".format(t))
    else:
        factor = []

        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                factor.append(i)
                if i != n//i:
                    factor.append(n//i)

        for i in factor:
            if i % 2 == 0 and (n//i) % 2 == 1:
                ans = [n//i, i]
                break
            elif i % 2 == 1 and (n//i) % 2 == 0:
                ans = [i, n//i]
                break
        print("Case {}: {} {}".format(t, ans[0], ans[1]))
