"""8. Crea el siguiente módulo:
 El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entre dos números. Todas ellas devolverán el resultado.
 En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se quede bloqueada una funcionalidad, eso incluye:
 TypeError: En caso de que se envíen valores a las funciones que no sean números. Además deberá aparecer un mensaje que informe Error: Tipo de dato no válido.
 ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe Error: No es posible dividir entre cero.
Una vez diseñado el modulo, desarrolle un programa que, utilizando el modulo anterior, haga uso de todas la funciones con los parámetros ingresados por teclado"""
from operaciones import *

def menu():
    desicion=int(input("Operaciones:\n1) Suma\n2) Resta\n3) Multiplicación\n4) Division\nIngrese la operacion que desea realizar: "))
    while True: 
        try:
            a=int(input("Ingrese un numero: "))
            break
        except ValueError:
            print("debe ser un numero")
           
    while True:
        try:
            b=int(input("Ingrese otro numero: "))
            break
        except ValueError:
            print("debe ser un numero")
        
    if desicion==1:
       print(f"esto es una suma! {suma(a,b)}")
       
    if desicion==2:
       print(f"esto es una resta! {resta(a,b)}")
    
    if desicion==3:
       print(f"esto es una multiplicacion! {producto(a,b)}")
       
    if desicion==4:
        while True:
                try: 
                    print(f"esto es una division! {division(a,b)}")
                    break
                except ZeroDivisionError:
                    while True:    
                        try:
                            print("No es posible dividir por cero, ingrese otro numero: ")
                            b=int(input())
                            break
                        except ValueError:
                            print("Debe ser un numero")
                        except ZeroDivisionError:
                            pass
                                       
menu()