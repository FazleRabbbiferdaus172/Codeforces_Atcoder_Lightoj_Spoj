for _ in range(int(input())):
    n = int(input())

    l = list(map(int, input().split()))
    odd, even = [], []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    if len(odd) % 2 == 1:
        odd.pop(-1)
    if len(even) % 2 == 1:
        even.pop(-1)

    new = odd[:] + even[:]
    # print(new)
    for i in range(0, 2*(n-1), 2):
        #print("it's i:", i)
        a, b = l.index(new[i]), l.index(new[i+1])
        print(a+1, b+1)
        l[a] = '$'
        l[b] = '$'
