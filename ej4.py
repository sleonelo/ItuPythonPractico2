"""Escriba una función en Python que reciba una lista de valores enteros y devuelva otra lista sólo con aquellos valores pares.
Ej.:
Entrada: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Salida: [2, 4, 6, 8]"""

def filtro_par(lista):
    nueva=[]
    for i in lista:
        if i%2==0:
            nueva.append(i)
            
    return(nueva)
    
print(filtro_par([1, 2, 3, 4, 5, 6, 7, 8, 9,10]))
            
