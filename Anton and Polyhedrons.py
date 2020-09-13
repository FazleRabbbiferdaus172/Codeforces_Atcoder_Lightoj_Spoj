d = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8,
     "Dodecahedron": 12, "Icosahedron": 20}

n = int(input())

t_n_f = 0

for _ in range(n):
    t_n_f += d[input()]

print(t_n_f)
