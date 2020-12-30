r, x, y, nx, ny = map(int, input().split())

dist = ((nx-x)**2+(ny-y)**2)**0.5
add = 0
if dist % (2*r) != 0:
    add = 1
print(int(dist//(2*r)) + add)
