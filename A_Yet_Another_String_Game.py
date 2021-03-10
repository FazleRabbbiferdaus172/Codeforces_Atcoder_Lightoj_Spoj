for _ in range(int(input())):
    s = input()
    ans = []
    for i in range(len(s)):
        if i % 2 == 0:
            x = ord('a')
            while x == ord(s[i]):
                x += 1
            ans.append(chr(x))
        else:
            x = ord('z')
            while x == ord(s[i]):
                x -= 1
            ans.append(chr(x))
    print("".join(ans))
