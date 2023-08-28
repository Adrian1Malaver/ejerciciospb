from validar_numero import validar_numero

try:
    numero = input("Ingrese un número: ")
    base = int(input("Ingrese la base (2, 8, 10 o 16): "))

    if validar_numero(numero, base):
        print("El número es válido en la base", base)
    else:
        print("El número NO es válido en la base", base)
except ValueError as e:
    print(e)
