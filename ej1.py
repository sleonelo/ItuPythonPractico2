"""Escriba una función en Python que indique si un número está en un determinado rango de numeros.
Ej.:
Entrada: valor=3; lim_inferior=2; lim_superior=5
Salida: True"""
valor=4
def rango (lim_inferior,lim_superior):
    if valor>lim_inferior and valor<lim_superior:
        return True

print(rango(2,5))