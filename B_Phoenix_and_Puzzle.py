def isPowerOfTwo(x):

    return (x and (not(x & (x - 1))))


for _ in range(int(input())):
    x = int(input())
    if (x/2)**.5 == int((x/2)**.5) or (x/4)**.5 == int((x/4)**.5):
        print("YES")
    else:
        print("NO")
