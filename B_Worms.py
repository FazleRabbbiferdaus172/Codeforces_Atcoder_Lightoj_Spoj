n = int(input())
a = list(map(int, input().split()))
m = int(input())
j = list(map(int, input().split()))
lasn = [0]*n
lasn[0] = a[0]
for i in range(1, n):
    lasn[i] = lasn[i-1] + a[i]
# print(lasn)
for i in j:
    lef = 0
    ri = n-1
    while lef < ri:
        mid = (lef+ri)//2
        if i <= lasn[mid]:
            ri = mid
        else:
            lef = mid + 1
        #print(lef, ri, mid, lasn[mid], i)
    print(ri+1)
