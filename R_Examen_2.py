import numpy as np

# Función para leer la matriz A y el vector B de archivos de texto


def leer_archivos():
    with open('A.txt', 'r') as file_A:
        first_line_A = file_A.readline().strip().split()
        # Obtener filas y columnas para A
        rows_A, cols_A = map(int, first_line_A)

        # Leer el resto del archivo y construir la matriz A
        A = []
        for _ in range(rows_A):
            line = file_A.readline().strip()
            row_values = list(map(float, line.split()))
            A.append(row_values)

        A = np.array(A)

    with open('B.txt', 'r') as file_B:
        # Leer el tamaño del vector B
        num_elements_B = int(file_B.readline().strip())

        # Leer los elementos del vector B
        B = []
        for _ in range(num_elements_B):
            line = file_B.readline().strip()
            B.append(float(line))

        # Darle forma de columna (vector)
        B = np.array(B).reshape((num_elements_B, 1))

    return A, B

# Métodos de solución


def eliminacion_gaussiana(a, b):
    n = len(b)

    # Combinar las matrices a y b en una sola matriz aumentada
    matriz_aumentada = np.concatenate((a, b), axis=1)

    # Eliminación hacia adelante
    for i in range(n):
        # pivoteeo parcial: intercambiar filas si es necesario para evitar divisiones por cero
        if matriz_aumentada[i, i] == 0:
            for j in range(i + 1, n):
                if matriz_aumentada[j, i] != 0:
                    matriz_aumentada[[i, j]] = matriz_aumentada[[j, i]]
                    break

        # Eliminación gaussiana
        pivote = matriz_aumentada[i, i]
        for j in range(i + 1, n):
            factor = matriz_aumentada[j, i] / pivote
            matriz_aumentada[j] -= factor * matriz_aumentada[i]

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (matriz_aumentada[i, n] - np.dot(matriz_aumentada[i,
                i + 1:n], x[i + 1:])) / matriz_aumentada[i, i]

    return x


def factorizacion_lu(a, b):
    n = len(a)
    # Inicializar las matrices L y U
    l = np.zeros((n, n))
    u = np.zeros((n, n))

    # Factorización LU
    for i in range(n):
        l[i, i] = 1  # Diagonal de L es 1
        for j in range(i, n):
            u[i, j] = a[i, j] - np.dot(l[i, :i], u[:i, j])
        for j in range(i + 1, n):
            l[j, i] = (a[j, i] - np.dot(l[j, :i], u[:i, i])) / u[i, i]

    # Resolver Ly = b mediante sustitución hacia adelante
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(l[i, :i], y[:i])

    # Resolver Ux = y mediante sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(u[i, i + 1:], x[i + 1:])) / u[i, i]

    return x


# Variables
metodo_valido = False  # Identificar que el método sea correcto
# Programa principal
A, B = leer_archivos()

# Se le pide al usuario que elija un método
print("Elija un método de solución:")
print("1. Eliminación de Gauss")
print("2. Factorización LU")

while not metodo_valido:
    eleccion = int(input("Ingrese el número del método: "))
    if (eleccion < 1 or eleccion > 2):
        print("Método no valido")
    else:
        metodo_valido = True

if eleccion == 1:
    X = eliminacion_gaussiana(A, B)
    metodo = "Eliminación de Gauss"
elif eleccion == 2:
    X = factorizacion_lu(A, B)
    metodo = "Factorización LU"

# Imprimir los resultados
print(f"Método utilizado: {metodo}")
print("Solución del sistema: ")
for i, x in enumerate(X, start=1):
    print(f"x{i} = {x}")
