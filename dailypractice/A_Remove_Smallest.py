for i in range(int(input())):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    for i in range(n-1):
        if l[i] + 1 < l[i+1]:
            print("NO")
            break
    else:
        print("YES")
