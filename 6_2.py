"""Los empleados de una fábrica trabajan en dos turnos, Diurno y Nocturno. Se desea calcular el jornal diario de acuerdo a las siguientes reglas:
 La tarifa de las horas diurnas es de $350
 La tarifa de las horas nocturnas es de $400
 En caso de ser festivo, la tarifa se incrementa en un 10% en caso de turno diurno y en un 15% para el nocturno.
Desarrolle una función que permita ingresar por teclado la siguiente información para, al menos, 2 empleados, nombre del trabajador, el número de horas trabajadas, el turno y el tipo de día (“Festivo”, “Laborable”), para ello se podría utilizar 1 “diccionario” para registrar la información y si los datos ingresados son correctos llamar a otra función que realice el cálculo del sueldo a cobrar en ese día. Mostrar por pantalla los datos ingresados y el sueldo calculado para cada empleado."""
datos_empleado={}
lista_datos=[]
while True:
    nomb=input("ingrese nombre del empleado: ")
    while True:
        try:
            horas=int(input("Ingrese numero de horas trabajadas: "))
        except ValueError:
            print("debes ingresar un numero!!!")
            continue
        break
    turno=input("tipo de turno diurno o nocturno (D/N)")
    while turno.upper() not in ("D","N"):
        turno=input("tipo de turno diurno o nocturno (D/N)")
    dia=input("tipo de dia laborable o festivo (L/F)")
    while dia.upper() not in ("L","F"):
        dia=input("tipo de dia laborable o festivo (L/F)")
         
    def empleado(nomb,horas,turno,dia):
        datos_empleado[nomb]=[horas,turno,dia]
        lista_datos.append(datos_empleado)
        if len(lista_datos)>1:
            lista_datos.pop()
        return lista_datos#lista_empleados
        
    def calculo(lista_datos):
        for i in lista_datos:
            trabajador=i.keys()
            datos=list(i.values())
        for i in range (len(datos)):
            if datos[i]=="N":
                if datos[i+1]=="F":
                    print("funciona")
                
            #(f"el empleado {datos_empleado.keys()} debe cobrar: {datos_empleado[0]*1.15*400}")      
    
    empleado(nomb,horas,turno,dia) 
    calculo(lista_datos)
    
            