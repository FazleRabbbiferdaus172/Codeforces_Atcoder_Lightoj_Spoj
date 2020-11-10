for _ in range(int(input())):
    n = int(input())

    l = [int(x) for x in input().split()]

    l.sort(reverse=True)
    k = n - 2
    while min(l[0], l[1]) < k+1 and k > 0:
        k -= 1

    print(k)
