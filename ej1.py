"""Escriba una función en Python que indique si un número está en un determinado rango de numeros.
Ej.:
Entrada: valor=3; lim_inferior=2; lim_superior=5
Salida: True"""
lim_inferior=input("ingrese inicio del rango: ")
lim_superior=input("ingrese fin del rango: ")
valor=input("ingrese un valor: ")

def rango (lim_inferior,lim_superior,valor):
    if valor>=lim_inferior and valor<=lim_superior:
        return True
        #print(f"{valor} esta dentro del rango")
    else:
        return False
        #print(f"{valor} no esta dentro del rango")

rango(lim_inferior,lim_superior,valor)
