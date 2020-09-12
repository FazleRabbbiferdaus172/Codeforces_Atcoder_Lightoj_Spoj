
t = int(input())

for w in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    print(max(l[0]*l[1]*l[2]*l[3]*l[-1], l[0]*l[1]*l[-3]
              * l[-2]*l[-1], l[-1]*l[-2]*l[-3]*l[-4]*l[-5]))
