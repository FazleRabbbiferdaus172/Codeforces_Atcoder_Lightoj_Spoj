for _ in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))

    l = [i % 2 for i in l]
    odd = l.count(1)
    even = n - odd
    z = min(x, odd)
    ans = "No"
    for i in range(1, z+1, 2):
        if x - i <= even:
            ans = "Yes"
            break
    print(ans)
