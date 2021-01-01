n = int(input())

n -= 1
count = 0
ans_pos = 0
i = 1
while n >= 0:
    ans_pos = n
    n -= i
    print(i, ans_pos, n)
    i += 1
    count += 1


print(ans_pos+1)
