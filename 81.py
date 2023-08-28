"""ejercicio #81: Crear un módulo de funciones aritméticas que realicen las operaciones de suma, resta,
multiplicación, división y potencia de enteros, escribir un programa que importe este
módulo y use estas funciones para operar con números capturados desde el teclado.
"""
#definimos funciones aritmeticas
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def potenciacion(a,b):
    return a**b

#pedimos dos numeros a operar
n1=float(input("ingrese el primer numero: "))
n2=float(input("ingrese el segundo numero: "))

#mostramos tipos de operaciones aritmeticas
print("1 para suma")
print("2 para resta")
print("3 para multiplicacion")
print("4 para division")
print("5 para potenciacion")
print(" ")

#pedimos tipo de operacion aritmetica
op=int(input("elija una opcion: "))

#invocamos funcion y mostramos resultados
if op==1:
    print("la suma de los terminos ",n1," y ",n2," es: ", suma(n1,n2))
if op==2:
    print("la resta de los terminos ",n1," y ",n2," es: ", resta(n1,n2))
if op==3:
    print("la multiplicacion de los terminos ",n1," y ",n2," es: ", multiplicacion(n1,n2))
if op==4:
    print("la division de los terminos ",n1," y ",n2," es: ", division(n1,n2))
if op==5:
    print("la potenciacion de los terminos ",n1," y ",n2," es: ", potenciacion(n1,n2))
   
    
        
