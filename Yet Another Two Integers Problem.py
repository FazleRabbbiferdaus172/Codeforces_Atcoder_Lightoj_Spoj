t = int(input())

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    r = abs(b-a) // 10
    if abs(b-a) % 10:
        r += 1

    print(r)
