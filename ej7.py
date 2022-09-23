"""Realice el ejercicio 12 del practico numero 1, pero implementando la/s función/es necesaria/s."""
"""Escribir un programa que permita cargar y procesar datos de alumnos del ITU en una lista de tuplas con la siguiente forma: (nombre, dni, materia). Ejemplo: [(“Manuel Juarez”, 19823451, “Matematica”), (“Silvana Paredes”, 22709128, “Programacion”), (“Rosa Ortiz”, 15123978, “Redes”), (“Luciana Hernandez”, 38981374, “Programacion”)]. Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
 Agregar alumnos a la lista.
 Dado el DNI de un alumno, ver las materias que cursa.
 Dada una materia, mostrar la cantidad de alumnos que la cursan.
"""



alumno={}
dat=[]
while True:
    
    desicion=int(input("\n1_Ingresar un alumno \n2_Materias que cursa el alumno: \n3_Materia por alumno\n4_Lista de alumnos\n\nSeleccione un numero: "))
    
    if desicion==1:
        nom=input("ingrese nombre: ")
        dni=int(input("ingrese dni: "))
        mat=input("ingrese materia: ")
        continue

    
    if desicion==2:
        ingDni=int(input("ingrese el dni para ver la materias que cursa: "))
        for i in dat.values():
         if ingDni in dat.values():
                print(dat.keys())
                continue
    
    def datos(nom,dni,mat):
        alumno[nom]=[dni,mat]
        dat.append(alumno)
        for i in range(len(dat)):
            if len(dat)>1:
                dat.pop()
        return(dat)                       
    
    datos(nom,dni,mat)
        
    
    

"""
contador=0
desicion1="si"
alumnos1=[]
alumnos=[("lala",123,"matematica"),("lele",456,"matematica"),("lili",789,"matematica"),("lolo",101112,"matematica")]
tupla=()
desicion2=int(1)


while True:
    
    desicion=int(input("\n1_Ingresar un alumno \n2_Materias que cursa el alumno: \n3_Materia por alumno\n4_Lista de alumnos\n\nSeleccione un numero: "))
    
    if desicion==1:
        cargaNom=input("ingrese nombre: ")
        alumnos1.append(cargaNom)
        cargaDni=int(input("ingrese dni: "))
        alumnos1.append(cargaDni)
        cargaMat=input("ingrese materia: ")
        alumnos1.append(cargaMat)
        tupla=tuple(alumnos1)
        alumnos.append(tupla)
        print(alumnos)
        alumnos1.clear()
        continue

    if desicion==2:
        ingDni=int(input("ingrese el dni para ver la materias que cursa: "))
        for i in range(len(alumnos)):
         if ingDni in alumnos[i]:
                print(alumnos[i][2])
                continue
    
    if desicion==3:
        ingMat=input("ingrese una materia para ver el numero de cursantes: ")
        for i in range(len(alumnos)):
            if ingMat in alumnos[i]:
                contador+=1
        print(f"cantidad de cursantes: {contador}")
        continue           
    
    if desicion==4:
        print(alumnos)
        continue"""