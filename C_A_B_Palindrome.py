for _ in range(int(input())):
    a, b = map(int, input().split())
    s = list(input())

    a = a - s.count('0')
    b = b - s.count('1')

    for i in range(len(s)//2):
        if s[i] != '?' and s[-(i+1)] != '?':
            continue
        if s[i] != '?' and s[-(i+1)] == '?':
            if s[i] == '1' and b > 0:
                s[-(i+1)] = '1'
                b -= 1
            elif s[i] == '0' and a > 0:
                s[-(i+1)] = '0'
                a -= 1
        elif s[i] == '?' and s[-(i+1)] != '?':
            if s[-(i+1)] == '1' and b > 0:
                s[i] = '1'
                b -= 1
            elif s[-(i+1)] == '0' and a > 0:
                s[i] = '0'
                a -= 1
        elif s[i] == '?' and s[-(i+1)] == '?':
            if a >= b and a > 1:
                s[i] = '0'
                s[-(i+1)] = '0'
                a -= 2
            elif b > 1:
                s[i] = '1'
                s[-(i+1)] = '1'
                b -= 2
    if len(s) % 2 == 1:
        x = len(s) // 2
        if s[x] == '?':
            if a > 0:
                s[x] = '0'
                a -= 1
            else:
                s[x] = '1'
                b -= 1
    #print("a,b", a, b)
    if '?' in s or a != 0 or b != 0:
        print(-1)
    elif s != s[::-1]:
        print(-1)
    else:
        print("".join(s))
