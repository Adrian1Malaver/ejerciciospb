def calcular_resultado(numero):
    resultado = numero ** 2 - 2 * numero
    return resultado

numero_ingresado = float(input("Ingrese un número: "))

resultado_calculado = calcular_resultado(numero_ingresado)

print("El resultado de restar el doble del número a su cuadrado es:", resultado_calculado)
