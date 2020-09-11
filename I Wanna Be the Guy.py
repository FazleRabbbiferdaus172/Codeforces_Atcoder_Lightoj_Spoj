n = int(input())

l = [int(x) for x in input().split()]
l = l[1:]
j = [int(x) for x in input().split()]
j = j[1:]
l += (j)
l = set(l)

if len(l) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
