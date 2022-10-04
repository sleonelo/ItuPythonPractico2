"""Realice el ejercicio 12 del practico numero 1, pero implementando la/s función/es necesaria/s."""
"""Escribir un programa que permita cargar y procesar datos de alumnos del ITU en una lista de tuplas con la siguiente forma: (nombre, dni, materia). Ejemplo: [(“Manuel Juarez”, 19823451, “Matematica”), (“Silvana Paredes”, 22709128, “Programacion”), (“Rosa Ortiz”, 15123978, “Redes”), (“Luciana Hernandez”, 38981374, “Programacion”)]. Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
 Agregar alumnos a la lista.
 Dado el DNI de un alumno, ver las materias que cursa.
 Dada una materia, mostrar la cantidad de alumnos que la cursan.
"""

opcion=int(input("1) Agregar alumno\n2) ver materia por dni\n3) mostrar alumnos que cursan una materia\nSeleccione un numero por favor: "))
print(f"usted selecciono {opcion}")


def accion(opcion):
    if opcion==1:
        agregar()        
    elif opcion==2:
        ver_materias()
            
    
    
def ver_materias(agregar):
    for i in agregar.values():
        print (i)    


def agregar():
    alumno={}
    nombre=input("ingrese nombre: ")
    dni=input("ingrese dni: ")
    materia=input("ingrese materia: ")
    alumno[nombre]=[dni,materia]
    print (alumno)
    
accion(1)    

