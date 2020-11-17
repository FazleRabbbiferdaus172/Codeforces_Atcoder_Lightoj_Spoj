for _ in range(int(input())):
    n, a, b = map(int, input().split())

    s = ""
    k = 'a'
    for i in range(b):
        s += chr(ord('a') + i)
    s = s*(a//b) + s[:a % b]
    ans = s*(n//a) + s[:n % a]

    print(ans)
