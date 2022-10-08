
"""def funcion_suma_sueldo ():
    diccionario_sueldo_años = {
    2019: 100000,
    2020: 110000,
    2021: 125000,
    2022: 140000
    }
    suma_sueldo = 0
    for sueldo in diccionario_sueldo_años.values():
        suma_sueldo += sueldo
    print ("SUMATORIA:  ", suma_sueldo)

funcion_suma_sueldo()"""

"""def funcion_suma_sueldo(parametro_diccionario):
    suma_sueldo = 0
    for sueldo in parametro_diccionario.values():
        suma_sueldo += sueldo
    return suma_sueldo

diccionario_sueldo_años = {
2019: 100000,
2020: 110000,
2021: 125000,
2022: 140000
}
calculo_sumatoria = funcion_suma_sueldo(diccionario_sueldo_años)
print ("Sumatoria de Sueldos devuelta por la Funcion: ", calculo_sumatoria)
"""
"""
trabajador={}
dato=[]
dato1=[]
while True:
    nombre=input("ingrese nombre: ")
    horas=int(input("ingrese horas: "))
    turno=input("ingrese turno: ")
    dia=input("ingrese dia: ")

    def datos(nombre, horas, turno, dia):
        dato.append(nombre)
        dato.append(horas)
        dato.append(turno)
        dato.append(dia)
                           
        print(dato)    
        
    def calculo(**dato):
        print(len(dato))
    
    
        
    datos(nombre, horas, turno, dia)
    calculo(dato)  
    continue
"""
# def funcion_prueba(**52,36,69,15,7):
#     print("Diccionario completo: ",parametros)
#     for clave in parametros.keys():
#         print (" Clave: ", clave, end=",")
#     total = 0
#     for value in parametros.values():
#         total += value
#         return total
#     valor_retornado = funcion_prueba(a=10, b=20, c=30, d=40, e=50)
#     print ("\nValor devuelto por la Funcion (1): " , valor_retornado)
#     valor_retornado = funcion_prueba(a=10, b=20)
#     # print ("\nValor devuelto por la Funcion (2): " , valor_retornado)

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for i in sorted(opciones):
        print(f' {i}) {opciones[i][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1', accion1),
        '2': ('Opción 2', accion2),
        '3': ('Opción 3', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('Has elegido la opción 1')


def accion2():
    print('Has elegido la opción 2')


def accion3():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()