for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]

    if not a % b:
        print("YES")
    else:
        print("NO")
