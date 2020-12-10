n, k, l, c, d, p, nl, np = map(int, input().split())


kl = k*l
pkl = kl//nl
cd = c*d
psp = p // np

ans = min(pkl, psp, cd)
print(ans//n)
