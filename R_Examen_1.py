import math

# Definición de las funciones


def f(x):
    return x**3 - 2*x**2 + 8*x - 1


valor_verdadero_f = 0.1288852300784


def g(x):
    return math.exp(-x) - x


valor_verdadero_g = 0.5671432877253


def h(x):
    return (1 - 0.6*x) / x


valor_verdadero_h = 1.6666663744053
# Definición de las derivadas (para el método de Newton-Raphson)


def df(x):
    return 3*x**2 - 4*x + 8


def dg(x):
    return -math.exp(-x) - 1


def dh(x):
    return (0.6 * x - 1) / x**2

# Métodos numéricos

# Método de la bisección


def biseccion(func, a, b, tol):
    if func(a) * func(b) >= 0:
        print("La bisección requiere que la función cambie de signo en el intervalo.")
        return None

    c = a
    iteraciones = 0

    while (b - a) / 2.0 > tol:
        iteraciones += 1
        c = (a + b) / 2.0

        if func(c) == 0:
            break

        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

    return c, func(c), iteraciones

# Método de la regla falsa con límite máximo de iteraciones


def regla_falsa(func, a, b, tol, max_iter=1000):
    if func(a) * func(b) >= 0:
        print("La regla falsa requiere que la función cambie de signo en el intervalo.")
        return None

    iteraciones = 0

    while iteraciones < max_iter:
        iteraciones += 1
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        if func(c) == 0 or abs(b - a) < tol:
            break

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return c, func(c), iteraciones

# Método de Newton-Raphson


def newton_raphson(func, derivada, x0, tol, max_iter):
    iteraciones = 0
    x = x0

    while abs(func(x)) > tol and iteraciones < max_iter:
        iteraciones += 1
        x = x - func(x) / derivada(x)

    return x, func(x), iteraciones

# Método de la secante


def secante(func, x0, x1, tol, max_iter):
    iteraciones = 0

    while abs(func(x1)) > tol and iteraciones < max_iter:
        iteraciones += 1
        # Manejo de la situación de posible división por cero
        if abs(func(x1) - func(x0)) < 1e-10:
            break
        sig_x = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        x0, x1 = x1, sig_x

    return x1, func(x1), iteraciones


# Método para sacar error relativo
def error_relativo(valor_verdadero, valor_calculado):
    return abs((valor_verdadero - valor_calculado) / valor_verdadero) * 100 if valor_verdadero != 0 else 0


# Pruebas y resultados


# Función f(x)
print("\n\n-------------Resultados función f(x)-------------")

# Bisección para la función f(x) en el intervalo [-3, 3]
raiz, valor_de_funcion_en_raiz, iteraciones = biseccion(f, -3, 3, 1e-5)
print("\nMétodo de Bisección para f(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función f en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_f, raiz)}")

# Regla Falsa para la función f(x) en el intervalo [-3, 3]
raiz, valor_de_funcion_en_raiz, iteraciones = regla_falsa(f, -3, 3, 1e-5)
print("\nMétodo de Regla Falsa para f(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función f en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_f, raiz)}")

# Newton-Raphson para la función f(x) con x0 = 1
raiz, valor_de_funcion_en_raiz, iteraciones = newton_raphson(
    f, df, 1, 1e-5, 100)
print("\nMétodo de Newton-Raphson para f(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función f en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_f, raiz)}")

# Secante para la función f(x) con x0 = -2 y x1 = -1
raiz, valor_de_funcion_en_raiz, iteraciones = secante(f, -2, -1, 1e-5, 100)
print("\nMétodo de la Secante para f(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función f en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_f, raiz)}")

# ---------------------------------------
# Función g(x)
print("\n\n-------------Resultados función g(x)-------------")

# Bisección para la función g(x) en el intervalo [0, 1]
raiz, valor_de_funcion_en_raiz, iteraciones = biseccion(g, 0, 1, 1e-5)
print("\nMétodo de Bisección para g(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función g en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_g, raiz)}")

# Regla Falsa para la función g(x) en el intervalo [0, 1]
raiz, valor_de_funcion_en_raiz, iteraciones = regla_falsa(g, 0, 1, 1e-5)
print("\nMétodo de Regla Falsa para g(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función g en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_g, raiz)}")

# Newton-Raphson para la función g(x) con x0 = 1
raiz, valor_de_funcion_en_raiz, iteraciones = newton_raphson(
    g, dg, 1, 1e-5, 100)
print("\nMétodo de Newton-Raphson para g(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función g en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_g, raiz)}")

# Secante para la función g(x) con x0 = -2 y x1 = -1
raiz, valor_de_funcion_en_raiz, iteraciones = secante(g, -2, -1, 1e-5, 100)
print("\nMétodo de la Secante para g(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función g en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_g, raiz)}")

# ---------------------------------------
# Función h(x)
print("\n\n-------------Resultados función h(x)-------------")

# Bisección para la función h(x) en el intervalo [1, 2]
raiz, valor_de_funcion_en_raiz, iteraciones = biseccion(h, 1, 2, 1e-5)
print("\nMétodo de Bisección para h(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función h en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_h, raiz)}")

# Regla Falsa para la función h(x) en el intervalo [1, 2]
raiz, valor_de_funcion_en_raiz, iteraciones = regla_falsa(h, 1, 2, 1e-5)
print("\nMétodo de Regla Falsa para h(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función h en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_h, raiz)}")

# Newton-Raphson para la función h(x) con x0 = 1
raiz, valor_de_funcion_en_raiz, iteraciones = newton_raphson(
    h, dh, 1, 1e-5, 100)
print("\nMétodo de Newton-Raphson para h(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función h en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_h, raiz)}")

# Secante para la función h(x) con x0 = -2 y x1 = -1
raiz, valor_de_funcion_en_raiz, iteraciones = secante(h, -2, -1, 1e-5, 100)
print("\nMétodo de la Secante para h(x)")
print(f"Raíz encontrada: {raiz}")
print(f"Valor de función h en la raíz: {valor_de_funcion_en_raiz}")
print(f"Iteraciones necesarias: {iteraciones}")
print(f"Error relativo: {error_relativo(valor_verdadero_h, raiz)}")
