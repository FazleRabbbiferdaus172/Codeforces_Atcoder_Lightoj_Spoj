s = input()
h, q, n = 1000, 1000, 1000
ans = "NO"
if "H" in s:
    h = s.index("H")
if "Q" in s:
    q = s.index("Q")
if "9" in s:
    n = s.index("9")

xx = min(h, q, n)

if xx < 1000:
    ans = "YES"

print(ans)
