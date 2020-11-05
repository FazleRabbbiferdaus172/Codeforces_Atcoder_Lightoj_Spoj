
prime = []
N = int(10e6)+1
mark = [0]*(N)

for i in range(3, N, 2):
    if not mark[i]:
        for j in range(3*i, N, i+i):
            mark[j] = 1
prime.append(2)
for i in range(3, N, 2):
    if not mark[i]:
        prime.append(i)

fi = []
for i in range(N):
    fi.append(i)

for i in prime:
    for j in range(i, N, i):
        fi[j] //= i
        fi[j] *= (i-1)


#prime = seieve()
# print(prime[:10])
for _ in range(int(input())):
    try:
        n = int(input())
    except:
        n = int(input())
    print(fi[n])
