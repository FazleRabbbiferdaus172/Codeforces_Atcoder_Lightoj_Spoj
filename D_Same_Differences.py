for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            temp = l[i+1:]
            temp_x = l[i] + (j-i)
            #print("temp_x: ", temp_x, "l[i]: ", l[i], "(j-i)", (j-i))
            if temp_x == l[j]:
                ans += 1
    print(ans)
