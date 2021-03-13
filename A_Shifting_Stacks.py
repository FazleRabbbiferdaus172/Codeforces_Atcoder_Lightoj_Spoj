for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = l[0]
    for i in range(1, n):
        s += l[i]
        if s < (i*(i+1))//2:
            print("NO")
            break
    else:
        print("YES")
