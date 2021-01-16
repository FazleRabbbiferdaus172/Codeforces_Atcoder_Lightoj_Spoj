def is_p(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
ans = []
for i in range(n, -1, -1):
    if is_p(i):
        ans += [i]
        n -= i
        break


for i in range(2, n+1):
    if is_p(i) and is_p(n-i):
        ans.append(i)
        if n - i != 0:
            ans.append(n-i)
        break

print(len(ans))
print(*ans)
