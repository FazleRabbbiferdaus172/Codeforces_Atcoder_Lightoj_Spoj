for _ in range(int(input())):
    n = int(input())

    l = list(map(int, input().split()))

    l.sort(reverse=True)
    ll = []
    for i in range(1, n):
        ll.append(l[i-1]-l[i])

    print(min(ll))
