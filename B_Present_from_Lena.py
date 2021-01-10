n = int(input())
mid = 2*n+1
ans = []
for i in range(n+1):
    x = ""
    k = 0
    for j in range(2*n+1):
        #print(j, (2*n+1)//2+1 - i, (2*n+1)//2+1 + i)
        # if j >= (2*n+1)//2+1 - i and j <= (2*n+1)//2+1 + i:
        #print(j, end=" ")
        # else:
        #print(" ", end=" ")
        if j >= (2*n+1)//2 - (i % (n+1)) and j <= (2*n+1)//2 + (i % (n+1)):
            if j < n:
                x += str(k) + " "
                k += 1
            elif j == n:
                x += str(k) + " "
            else:
                k -= 1
                # print(k)
                x += str(k) + " "
        elif j < (2*n+1)//2 - (i % (n+1)):
            x += "  "
        else:
            continue
    x = list(x)
    x.pop(-1)
    x = "".join(x)
    ans += [x]

for i in range(n-1, -1, -1):
    ans.append(ans[i])

for i in ans:
    print(i)
