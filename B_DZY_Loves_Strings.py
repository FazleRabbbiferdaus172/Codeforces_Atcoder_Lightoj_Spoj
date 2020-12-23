s = input()
k = int(input())
w = list(map(int, input().split()))
mp = dict()
x = 'a'
for i in range(len(w)):
    mp[chr(i+ord('a'))] = w[i]

ans = 0
ln = len(s)
for i in range(ln):
    ans += mp[s[i]]*(i+1)
# print(ans)
mx = max(w)
ml = ln + k
mul = (ml*(ml+1))//2 - (ln*(ln+1))//2
ans += mul*mx
print(ans)
