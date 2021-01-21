n = list(input())
rem = -1
for i in range(len(n)-1):
    if n[i] == '1' and n[i+1] == "0":
        rem = i+1
        break

n.pop(rem)
print("".join(n))
