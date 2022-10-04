"""10. Como ejercicio, escriba una función que use la funcion tomaNumero para leer un número del teclado y que maneje la excepción ErrorNumeroMalo."""

class ErrorNumeroMalo(BaseException):
    def __init__(self, message):
        self.message = message
        
def elige_numero():
    numero = input("Escriba un número: ")
    if numero == str(17):
        raise ErrorNumeroMalo("El 17 es malévolo")
    return numero

elige_numero()