"""9. Cree un programa que pida por teclado el ingreso de un usuario y contraseña, luego de ello utilice las funciones validaUsuario y validaClave, ambas en un módulo llamado seguridad. Dichas funciones deben realizar lo siguiente:
validaUsuario:
 El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
 El nombre de usuario debe ser alfanumérico. Si no lo cumple indicar el mensaje: “El nombre de usuario puede contener solo letras y números”
 Nombre de usuario válido, retorna True
validaClave:
 La contraseña debe contener un mínimo de 8 caracteres
 Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico
 La contraseña no puede contener espacios en blanco
 Contraseña válida, retorna True
 Contraseña no válida, retorna el mensaje: “La contraseña elegida no es segura”"""

nombre=input("Ingrese su usuario: ")

def validaUsuario(nombre):
    
    while len(nombre)<5 or len(nombre)>=12:
        print("el nombre debe contener entre 6 y 12 caracteres, ingrese un nuevo nombre: ")
        nombre=input()
        break
    while True:
        if not nombre.isalpha():
            break
        else:
            print ("El nombre de usuario debe contener letras y números, ingreselo nuevamente")
            nombre=input()
            
    while True:
        if nombre.isalnum():
            print("\nNombre correctamente ingresado!")
            break
        else:
            print ("El nombre de usuario debe contener letras y números, ingreselo nuevamente")
            nombre=input()    
    return(nombre)
        
validaUsuario(nombre) 

cont=input("contraseña: ")

def validaClave(cont):
    espSim =['$', '@', '#', '%'] 
    valor = True
      
    if len(cont) < 6: 
        print('La contraseña debe tener al menos 8 caracteres') 
        valor = False
          
    if not any(i.isdigit() for i in cont): 
        print('La contraseña debe contener al menos un numero') 
        valor = False
          
    if not any(i.isupper() for i in cont): 
        print('La contraseña debe contener al menos una mayuscula') 
        valor = False
          
    if not any(i.islower() for i in cont): 
        print('La contraseña debe contener al menos una minuscula') 
        valor = False
          
    if not any(i in espSim for i in cont): 
        print('La contraseña debe contener al menos un simbolo $@#') 
        valor = False
    if valor: #si valor es true
        return valor 
    
validaClave(cont)