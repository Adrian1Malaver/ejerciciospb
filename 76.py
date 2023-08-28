"""ejercicio #76: Escriba un programa que calcule el factorial de un numero usando recursividad"""

#definir funcion
def factorial(numero):
    
#no hay factorial de negativos
    if numero<0:
        return "debe ser un entero positivo"
    
#factorial de 0 o 1 es igual a 1
    elif numero==0 or numero==1:
        return 1
    
#llamar a la funcion multiples veces hasta que n llegue a 1 (recursividad)
    elif numero>1:
        return numero*factorial(numero-1)
    
#ingresar numero e invocar funcion
numero=int(input("ingrese un numero entero positivo: "))
print("el factorial de ", numero, "es: ", factorial(numero))
    
