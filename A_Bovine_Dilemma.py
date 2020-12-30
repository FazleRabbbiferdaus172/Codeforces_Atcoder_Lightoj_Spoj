for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    arr = []
    for i in range(n):
        for j in range(n):

            a = (.5) * 1 * (abs(l[i]-l[j]))
            if i != j:
                if a not in arr:
                    c += 1
                    arr.append(a)

    print(c)
