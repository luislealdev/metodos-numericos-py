import numpy as np

# Función para calcular f(1.6) usando interpolación de Lagrange


def metodo_lagrange(x, f_x, grado, valor_x):
    resultado = 0.0
    polinomio = ""
    for i in range(grado + 1):
        termino = f_x[i]
        for j in range(grado + 1):
            if j != i:
                termino *= (valor_x - x[j]) / (x[i] - x[j])
        resultado += termino
        polinomio += f"({termino})" if termino >= 0 else f"(-{-termino})"
        if i != 0:
            polinomio += f" * (x - {x[i-1]})"

        if i != grado:
            polinomio += " + "
    return resultado, polinomio

# Función para calcular las diferencias divididas (coeficientes) para el método de Newton


def diferencias_divididas(x, f_x):
    n = len(x)
    coeficientes = f_x.copy()
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coeficientes[i] = (coeficientes[i] -
                               coeficientes[i - 1]) / (x[i] - x[i - j])
    return coeficientes

# Función para calcular f(1.6) usando interpolación de Newton


def metodo_newton(x, f_x, grado, valor_x):
    coeficientes = diferencias_divididas(x[:grado + 1], f_x[:grado + 1])
    resultado = coeficientes[grado]
    polinomio = f"{resultado}"
    for i in range(grado - 1, -1, -1):
        resultado = resultado * (valor_x - x[i]) + coeficientes[i]
        if (coeficientes[i] >= 0):
            polinomio += f" + {coeficientes[i]}"
        else:
            polinomio += f" - {-coeficientes[i]}"
        if i != 0:
            polinomio += f" * (x - {x[i-1]})"

    return resultado, polinomio

# Función principal


# Variables
metodo_valido = False  # Identificar que el método sea correcto
# Datos del ejemplo
valor_xues = np.array([0, .5, 1, 1.5, 2, 2.5])
fvalor_xues = np.array([1, 2.119, 2.910, 3.945, 3.5])
valor_x = 1.6  # Valor para el que queremos calcular f(1.6)
# Programa principal
grado = int(input("Ingrese el grado del polinomio (1, 2 o 3): "))
# Se le pide al usuario que elija un método
print("Elija un método de solución:")
print("1. Lagrange")
print("2. Newton")

while not metodo_valido:
    eleccion = int(input("Ingrese el número del método: "))
    if (eleccion < 1 or eleccion > 2):
        print("Método no valido")
    else:
        metodo_valido = True

if eleccion == 1:
    resultadoado, polinomio = metodo_lagrange(
        valor_xues, fvalor_xues, grado, valor_x)
    metodo = "Lagrange"
elif eleccion == 2:
    resultadoado, polinomio = metodo_newton(
        valor_xues, fvalor_xues, grado, valor_x)
    metodo = "Newton"

# Imprimir los resultados
print(f"Método utilizado: {metodo}")
print(f"Polinomio resultante: f(x) = {polinomio}")
print(f"f({valor_x}) calculado: {resultadoado}")
