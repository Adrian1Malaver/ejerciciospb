"""ejercicio #57: Escribir un programa que cuente las mayúsculas de una cadena de caracteres"""

#ingresar cadena de caracteres
palabra=str(input("ingrese una palabra: "))

#indice y contador de mayusculas
i=0
mayus=0

#recorrer cadena
while i<len(palabra):
    letra=palabra[i]
    
#identificar mayusculas y contarlas
    if letra.isupper()==True:
        mayus+=1
    i+=1
    
#mostrar cantidad mayusculas
print("la cantidad de letras mayusculas es: ", mayus)

    
