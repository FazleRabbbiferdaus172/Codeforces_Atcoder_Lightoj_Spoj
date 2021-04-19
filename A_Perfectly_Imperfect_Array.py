for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    for i in l:
        if i**.5 != int(i**.5):
            print("YES")
            break
    else:
        print("NO")
