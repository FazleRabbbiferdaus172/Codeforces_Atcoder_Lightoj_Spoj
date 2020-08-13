n = int(input())
l = [int(x) for x in input().split()]

for i in range(n):

    print(min(abs(l[i]-l[i-1]), abs(l[i-n+1]-l[i])),
          max(l[i]-l[0], l[-1]-l[i]))
