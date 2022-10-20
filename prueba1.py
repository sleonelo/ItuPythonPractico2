# cadena="la arañita de martita"

# if any(i=="a" for i in cadena):
#     print("no hay una 'z' bro")
    
    
# var=input("ingrese A o B: ")
# var=var.upper()
# print(var)
# while var not in ("A","B"):
#     var=input("ingrese A o B: ")


while True:
    nombre=str(input("\nIngrese nombre del empleado: "))
    while True:
     try:
         horas = int(input("Ingrese horas trabajadas: "))
         break
     except ValueError:
         print("Debes escribir un numero!")

    turno = int(input("Ingresar tipo de turno:\n1)Diurno\n2)Nocturno\nSeleccione una opcion: "))
    while turno not in(1,2):
        turno = int(input("\nIngresar tipo de turno:\n1)Diurno\n2)Nocturno\nSeleccione una opcion: "))

    tipo_d_dia = int(input("\nIngresar tipo de día:\n3)Laborable\n4)Festivo\nSeleccione una opción: "))
    while tipo_d_dia not in (3,4):
        tipo_d_dia = input("Ingresar tipo de día:\n3)Laborable\n4)Festivo\nSeleccione una opción: ")

    lista_tres= []

    def empleado(nombre, horas, turno, tipo_d_dia): #se encuentra dentro del while
        empleados = {}
        empleados[nombre]= [horas, turno, tipo_d_dia]
        lista_tres.append(empleados)
        return lista_tres

    def calculo(lista_tres):
        for i in lista_tres:
            trabajador = list(i.keys())
            datos = list(i.values())
            print(datos)
            for i in range(len(datos)):
                if 1 in datos[i] :
                    if 3 in datos[i]:
                        print(f"{trabajador[0]} debe cobrar la cantidad de: {datos[i][0]*350}")
                    else:
                        print(f"{trabajador} debe cobrar la cantidad de: {datos[i][0]*1.1*350}")
                else:
                    if i == 3:
                        print(f"{trabajador} debe cobrar la cantidad de: {datos[i][0]*400}")
                    else:
                        print(f"{trabajador} debe cobrar la cantidad de: {datos[i][0]*1.15*400}")



    empleado(nombre, horas, turno, tipo_d_dia)
    calculo(lista_tres)