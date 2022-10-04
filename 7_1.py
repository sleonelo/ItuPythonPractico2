def menu_principal():
    opciones = {
        '1': (' Agregar alumnos a la lista.', funcion1),
        # la acción es una llamada a submenu que genera un nuevo menú
        '2': (' Dado el DNI de un alumno, ver las materias que cursa.', funcion2),
        '3': (' Dada una materia, mostrar la cantidad de alumnos que la cursan.', funcion3),
        '4': (' Salir', salir)
    }   
    generar_menu(opciones, 4)
    
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()  # se imprime una línea en blanco para clarificar la salida por pantalla


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion,opciones):
    if opcion==4

def funcion1():
    print('Has elegido la opción 1')
    dic = {}
    alumnos = []
    nombre = input("ingrese nombre: ")
    dni = input("ingrese dni: ")
    materia = input("ingrese materia: ")
    dic[nombre] = [dni, materia]
    alumnos.append(dic)
    print(alumnos)


def funcion2():
    print('Has elegido la opción 2')


def funcion3():
    print('Has elegido la opción 3')


def funcionA():
    print('Has elegido la opción A')


def funcionB():
    print('Has elegido la opción B')


def salir():
    print('Saliendo')


menu_principal()
    