for _ in range(int(input())):
    s = input()
    ind = -1
    ans = 'YES'
    if 'a' not in s:
        print("NO")
    else:
        ind = s.find('a')
        l, r = ind - 1, ind + 1
        cur = ord('a') + 1

        while cur != ord('a') + len(s):
            if l >= 0 and s[l] == chr(cur):
                l -= 1
            elif r < len(s) and s[r] == chr(cur):
                r += 1
            else:
                ans = 'NO'
            cur += 1
        print(ans)
