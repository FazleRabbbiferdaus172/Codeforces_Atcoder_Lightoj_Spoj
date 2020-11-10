for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]

    l.sort()
    chk = l[0]*l[-1]
    flg = True
    for i in range(1, 2*n, 2):
        if l[i]*l[-1*(i+1)] != chk or l[i] != l[i-1] or l[-1*(i+1)] != l[-1*(i)]:
            flg = False
            break

    if flg:
        print("YES")
    else:
        print("NO")
