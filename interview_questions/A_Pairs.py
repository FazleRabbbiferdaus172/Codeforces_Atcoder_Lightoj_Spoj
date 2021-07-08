for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    even, odd = [], []

    for i in l:
        if i % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
    if len(odd) == n:
        print("Yes")
    else:
        print("No")
