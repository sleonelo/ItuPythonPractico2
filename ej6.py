"""Los empleados de una fábrica trabajan en dos turnos, Diurno y Nocturno. Se desea calcular el jornal diario de acuerdo a las siguientes reglas:
 La tarifa de las horas diurnas es de $350
 La tarifa de las horas nocturnas es de $400
 En caso de ser festivo, la tarifa se incrementa en un 10% en caso de turno diurno y en un 15% para el nocturno.
Desarrolle una función que permita ingresar por teclado la siguiente información para, al menos, 2 empleados, nombre del trabajador, el número de horas trabajadas, el turno y el tipo de día (“Festivo”, “Laborable”), para ello se podría utilizar 1 “diccionario” para registrar la información y si los datos ingresados son correctos llamar a otra función que realice el cálculo del sueldo a cobrar en ese día. Mostrar por pantalla los datos ingresados y el sueldo calculado para cada empleado."""



trabajador={}
dato=[]
dato1=[]
while True:
    nombre=input("ingrese nombre: ")
    horas=int(input("ingrese horas: "))
    turno=input("ingrese turno: ")
    dia=input("ingrese dia: ")

    def datos(nombre, horas, turno, dia):
        trabajador[nombre]=[horas,turno,dia]
        dato.append(trabajador)
        for i in range(len(dato)):
            if len(dato)>1:
                dato.pop()
        
        return(dato)    
        
    def calculo(dato):  
        for i in dato:    
            lista=list(i.values())
            trabajador=list(i.keys())
            for i in range(len(lista)):
                if "nocturno" in lista[i]:
                    if "festivo" in lista[i]:
                        print(trabajador[i], 400*1.15*lista[i][0])
                    else:
                        print(trabajador[i], 400*lista[i][0])
                else:
                    if "festivo" in lista[i]:
                        print(trabajador[i],350*1.10*lista[i][0])
                    else:
                        print(trabajador[i],350*lista[i][0])  
            
                
      
    datos(nombre, horas, turno, dia)
    calculo(dato)  
    continue
    


