for _ in range(int(input())):
    n = int(input())

    l = list(map(int, input().split()))
    x = set(map(int, input().split()))
    ans = "Yes"
    if len(x) != 2 and l != sorted(l):
        ans = "No"

    print(ans)
