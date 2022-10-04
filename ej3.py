"""Escriba una función en Python que reciba como parámetro una frase y 1 carácter, y devuelva si ese carácter se encuentra dentro de la frase. Además de ello, la función debe poder indicar la cantidad de palabras que hay en la frase."""

frase=input("ingrese una frase: ")
letra=input("ingrese una letra: ")

def oracion (frase,letra):
    if any(letra==i for i in frase):
        fragmentado=frase.split()
        return (f"la letra si aparece en la frase y la cantidad de palabras que tiene la frase es {len(fragmentado)}")
    
    #if letra in frase:
    #    fragmentado=frase.split()
    #    return (f"la letra si aparece en la frase y la cantidad de palabras que tiene la frase es {len(fragmentado)}")
    #return (f"la letra {letra} no esta en la frase...")   
    
    
print(oracion(frase, letra))