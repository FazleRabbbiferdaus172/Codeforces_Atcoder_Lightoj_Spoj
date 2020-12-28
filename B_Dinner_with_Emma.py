n, m = map(int, input().split())
street = []
for i in range(n):
    x = list(map(int, input().split()))
    street.append(x)

emma_ind, emma = -1, -1

for j, i in enumerate(street):
    mn = min(i)
    if mn > emma:
        emma = mn
        emma_ind = j


print(emma)
