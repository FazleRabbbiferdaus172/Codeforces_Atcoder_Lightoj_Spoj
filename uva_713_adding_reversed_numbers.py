for _ in range(int(input())):
    a, b = map(str, input().split())
    a, b = int(a[::-1]), int(b[::-1])
    s = list(str(a+b))
    while len(s) > 0 and s[-1] == '0':
        s.pop(-1)
    print("".join(reversed(s)))
