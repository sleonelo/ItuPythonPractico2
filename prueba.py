
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

try:
    horas=int(input("ingrese horas: "))
except ValueError:
    print("debes escribir un numero!")
