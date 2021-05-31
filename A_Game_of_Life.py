for _ in range(int(input())):
    n, m = map(int, input().split())
    m = min(n, m)
    s = list(input())
    for i in range(m):
        temp = s.copy()
        for i in range(n):
            count = 0
            if i+1 < n and s[i+1] == '1':
                count += 1

            if i - 1 >= 0 and s[i-1] == '1':
                count += 1
            if count == 1:
                temp[i] = '1'
        s = temp.copy()
    print("".join(s))
