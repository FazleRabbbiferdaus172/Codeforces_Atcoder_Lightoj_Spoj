def div(x):
    while x % 2 == 0:
        x //= 2
    if x > 1:
        return True
    return False


for _ in range(int(input())):
    n = int(input())
    if n % 2 == 1:
        print("YES")
    elif div(n):
        print("YES")
    else:
        print("NO")
