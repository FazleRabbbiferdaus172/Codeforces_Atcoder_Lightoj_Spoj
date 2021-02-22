n, k = map(int, input().split())
l = list(input())
if n == k and n == 1:
    print(0)
else:
    ans = []
    for i in range(n):
        if i == 0 and l[i] != '1' and k > 0:
            ans += ['1']
            k -= 1
        elif i != 0 and l[i] != '0' and k > 0:
            ans += ['0']
            k -= 1
        else:
            ans += [l[i]]
    print("".join(ans))
