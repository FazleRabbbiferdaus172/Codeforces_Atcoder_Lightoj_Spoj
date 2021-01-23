n = int(input())

l = list(map(int, input().split()))

sold = {25: 0, 50: 0, 100: 0}

for i in l:
    if i == 25:
        sold[25] += 1
    elif i == 50 and sold[25] >= 1:
        sold[50] += 1
        sold[25] -= 1
    elif i == 100 and sold[50] >= 1 and sold[25] >= 1:
        sold[100] += 1
        sold[50] -= 1
        sold[25] -= 1
    elif i == 100 and sold[25] >= 3:
        sold[100] += 1
        sold[25] -= 3
    else:
        print("NO")
        break
else:
    print("YES")
