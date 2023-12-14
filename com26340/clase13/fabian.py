import math

# Función para calcular la raíz cuadrada de un número
def calcular_raiz_cuadrada(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return "Número negativo, la raíz cuadrada no está definida."

# Función para calcular la potencia de un número
def calcular_potencia(base, exponente):
    return math.pow(base, exponente)

# Solicitar al usuario que ingrese un número
numero = float(input("Ingresa un número: "))
# Calcular y mostrar la raíz cuadrada
raiz_cuadrada = calcular_raiz_cuadrada(numero)
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")

# Solicitar al usuario que ingrese una base y un exponente
base = float(input("Ingresa la base: "))
exponente = float(input("Ingresa el exponente: "))

# Calcular y mostrar la potencia
potencia = calcular_potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {potencia}")