for _ in range(int(input())):
    n = int(input())
    ans = "NO"
    if n >= 111*(n % 11):
        ans = "YES"
    print(ans)
