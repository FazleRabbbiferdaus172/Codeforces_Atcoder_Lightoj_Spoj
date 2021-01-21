n, m = map(int, input().split())
ac = list(map(int, input().split()))
wc = list(map(int, input().split()))

acmx = max(ac)
acmn = min(ac)
wcmn = min(wc)

ans = -1

if 2*acmn <= acmx and wcmn > acmx:
    ans = acmx
elif 2*acmn > acmx and 2*acmn < wcmn:
    ans = 2*acmn
print(ans)
