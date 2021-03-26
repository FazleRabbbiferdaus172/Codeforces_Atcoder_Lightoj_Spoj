n = list(map(int, list(input())))
count = 0
while len(n) > 1:
    n = list(map(int, str(sum(n))))
    # print(n)
    count += 1
print(count)
