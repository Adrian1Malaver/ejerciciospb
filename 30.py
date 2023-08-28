"""ejercicio #30: Escribir un programa que sume los números comprendidos entre un rango suministrado por el usuario."""

#leer rango
inicio=int(input("ingrese numero de inicio sumatoria: "))
fin=int(input("ingrese numero de fin sumatoria: "))
b=0

#iterar suma en el rango
for i in range(inicio, fin):
    b=b+i
#mostrar resultado
print("la sumatoria total del rango es:", b)
