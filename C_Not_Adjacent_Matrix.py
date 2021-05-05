for _ in range(int(input())):
    n = int(input())
    ans = []
    if n == 2:
        print(-1)
    else:
        odd = [i for i in range(1, n*n+1, 2)]
        even = [i for i in range(2, n*n+1, 2)]
        mid = n*n // 2
        c = 0
        for i in range(n):
            for j in range(n):
                if c < mid:
                    print(even[0], end=" ")
                    even.pop(0)
                else:
                    print(odd[0], end=" ")
                    odd.pop(0)
                c += 1
            print()
