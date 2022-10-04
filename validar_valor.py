#variable que indica si el valor es válido
#inicialmente no lo es
valido = False

#función para validar un dato
#def validar(valor):
#	return False #de momento está sin implementar y devolvemos siempre False
def validar(valor):
	entero = int(valor)
	return entero >= 0 and entero <= 100
#mensaje para que el usuario sepa que le solicitamos un valor

print('Introduzca un valor, por favor: ', end='')

#bucle para pedir el valor
while not valido: #mientras que no (en este caso valido=false... seria mientras que no sea falso)
	valor = input()#es igual al valor que introdujo el usuario no necesita una variable
	valido = validar(valor)
	if not valido: #if inverso osea que prueba si una condicion es falsa ejecuta(al reves)
		print('Lo siento, el valor no es válido, vuelva a intentarlo: ', end='')

#a partir de aquí sabemos que el valor es válido y ya podemos utilizarlo
print(f'El valor válido es {valor}.')