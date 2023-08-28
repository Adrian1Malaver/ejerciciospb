"""ejercicio #45: Escribir un programa que tras asignar números enteros a una lista, determine la posición de 
la lista en la que se encuentra el máximo valor."""

#pedir longitud lista
cantidad=int(input("cuantos numeros desea ingresar: "))

#crear lista
numeros=[]

#crear comparativo
b=0

#pedir numeros y almacenar en lista
for x in range(0, cantidad):
    numero=int(input("ingrese numero: "))
    numeros.append(numero)
    
#hallar valor maximo
    if b<numero:
        b=numero
        
#hallar posicion valor maximo
for i in range(0, len(numeros)):
    if b==numeros[i]:
        max=i
        
#mostrar posicion
print("el valor maximo se encontro en la pocision: ", max)


    
    


    
    
