for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]

    if a == 1 or b <= 1 or (a == 2 and b == 2):
        print("YES")
    else:
        print("NO")
