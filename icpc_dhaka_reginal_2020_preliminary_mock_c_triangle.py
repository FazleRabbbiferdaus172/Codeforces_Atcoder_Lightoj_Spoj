s = set(map(int, input().split()))

if len(s) == 1:
    print("Equilateral Triangle")
elif len(s) == 2:
    print("Isosceles Triangle")
else:
    print("Bad Triangle")
