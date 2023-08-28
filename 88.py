def cargar_alumnos():
    alumnos = []
    try:
        with open('alumnos.txt', 'r') as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera, estado = linea.strip().split(',')
                alumnos.append({'codigo': codigo, 'nombre': nombre, 'apellido': apellido, 'carrera': carrera, 'estado': estado})
    except FileNotFoundError:
        pass
    return alumnos

def guardar_alumnos(alumnos):
    with open('alumnos.txt', 'w') as archivo:
        for alumno in alumnos:
            archivo.write(f"{alumno['codigo']},{alumno['nombre']},{alumno['apellido']},{alumno['carrera']},{alumno['estado']}\n")

def agregar_alumno(alumnos):
    codigo = input("Ingrese el código del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    estado = input("Ingrese el estado del alumno: ")
    alumnos.append({'codigo': codigo, 'nombre': nombre, 'apellido': apellido, 'carrera': carrera, 'estado': estado})
    guardar_alumnos(alumnos)
    print("Alumno agregado exitosamente.")

def modificar_alumno(alumnos, codigo):
    encontrado = False
    for alumno in alumnos:
        if alumno['codigo'] == codigo:
            nombre = input("Ingrese el nuevo nombre del alumno: ")
            apellido = input("Ingrese el nuevo apellido del alumno: ")
            carrera = input("Ingrese la nueva carrera del alumno: ")
            estado = input("Ingrese el nuevo estado del alumno: ")
            alumno['nombre'] = nombre
            alumno['apellido'] = apellido
            alumno['carrera'] = carrera
            alumno['estado'] = estado
            guardar_alumnos(alumnos)
            print("Información del alumno modificada exitosamente.")
            encontrado = True
            break
    if not encontrado:
        print("Alumno no encontrado.")

def eliminar_alumno(alumnos, codigo):
    alumnos = [alumno for alumno in alumnos if alumno['codigo'] != codigo]
    guardar_alumnos(alumnos)
    print("Alumno eliminado exitosamente.")

def main():
    alumnos = cargar_alumnos()

    while True:
        print("\n1. Agregar alumno\n2. Modificar alumno\n3. Eliminar alumno\n4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_alumno(alumnos)
        elif opcion == '2':
            codigo = input("Ingrese el código del alumno a modificar: ")
            modificar_alumno(alumnos, codigo)
        elif opcion == '3':
            codigo = input("Ingrese el código del alumno a eliminar: ")
            eliminar_alumno(alumnos, codigo)
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()
