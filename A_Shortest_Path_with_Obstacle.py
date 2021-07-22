for _ in range(int(input())):
    dummy = input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())
    ans = abs(xa-xb) + abs(ya-yb)
    if (xa == xb == xf and yf < max(ya, yb) and yf > min(ya, yb)) or (ya == yb == yf and xf < max(xa, xb) and xf > min(xa, xb)):
        ans += 2

    print(ans)
