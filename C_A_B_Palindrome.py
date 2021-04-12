for _ in range(int(input())):
    a, b = map(int, input().split())
    s = list(input())
    d = {'0': a - s.count('0'), '1': b - s.count('1')}
    for i in range(len(s)//2):
        if s[i] != '?' and s[-(i+1)] != '?' and s[i] != s[-(i+1)]:
            s = ["-1"]
            break
        if s[i] != '?' and s[-(i+1)] == '?':
            s[-(i+1)] = s[i]
            d[s[i]] -= 1
        elif s[i] == '?' and s[-(i+1)] != '?':
            s[i] = s[-(i+1)]
            d[s[i]] -= 1

    if len(s) % 2 == 1:
        x = len(s) // 2
        if s[x] == '?':
            if d['1'] % 2 == 0 and d['0'] % 2 == 0:
                s = ["-1"]
            elif d['1'] % 2 == 1:
                s[x] = '1'
                d['1'] -= 1
            else:
                s[x] = '0'
                d['0'] -= 1

    for i in range(len(s)//2):
        if s[i] == '?' and s[-(i+1)] == '?' and d['1'] > 1:
            s[i] = '1'
            s[-(i+1)] = '1'
            d['1'] -= 2
        elif s[i] == '?' and s[-(i+1)] == '?' and d['0'] > 1:
            s[i] = '0'
            s[-(i+1)] = '0'
            d['0'] -= 2
        elif s[i] == '?' and s[-(i+1)] == '?' and d['0'] <= 1 and d['1'] <= 1:
            s = ['-1']
            break

    if s.count('0') != a or s.count('1') != b:
        s = ['-1']
    print("".join(s))
