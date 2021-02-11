n, k = map(int, input().split())

at = 4*60 - k
i = 0
#print("at", at)
while n > i and at >= 5*i:
    i += 1
    #print(at, 5*i)
    at -= 5*i
if at < 0:
    i -= 1
print(i)
