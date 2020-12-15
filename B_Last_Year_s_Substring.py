for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = "NO"
    #print(s[:4], s[-1])
    if s[0:2] == '20' and s[n-2:] == "20":
        #ll = s[len(s)-2:]
        # print(ll)
        # if '20' in ll:
        ans = "YES"
    if s[0] == '2' and s[n-3:] == "020":
        #ll = s[len(s) - 3:]
        # print(ll)
        # if '020' in ll:
        ans = "YES"
    if s[:3] == '202' and s[-1] == '0':
        # print(s[-1])
        # if s[-1] == '0':
        ans = "YES"
    if s[:4] in "2020":
        ans = "YES"
    if s[len(s) - 4:] == '2020':
        ans = "YES"
    print(ans)
