"""Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""

print("ingrese una frase: ")
def transformadora(frase):
    diccionario={}
    nueva=frase.split()
    for i in nueva:
        diccionario[i]=len(i)
    
    return(diccionario)

print(transformadora(input()))