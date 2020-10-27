for _ in range(int(input())):
    l, r = [int(x) for x in input().split()]
    #print((r+1)/2, l)
    if l >= r//2+1:
        print("YES")
    else:
        print("NO")
