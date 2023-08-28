numeros = []
for i in range(5):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

media = sum(numeros) / 5

print("La media aritmética de los números es:", media)