"""ejercicio #66: Escribir un programa que calcule el factorial de un numero leído desde el teclado usando 
funciones"""

#definir funcion
def factorial(numero):
    
#no hay factorial de negativos
    if numero<0:
        return "debe ser un numero entero positivo"
    
#factorial de 0 o 1 es igual a 1
    elif numero==0 or numero==1:
        return 1
    
#factorial de numero mayor a 1
    elif numero>1:
        for i in range(1, numero):
            numero*=i
    return numero

#pedir numero e invocar funcion
numero=int(input("ingrese un numero entero positivo: "))
print("el factorial del numero ", numero, "es: ", factorial(numero))


