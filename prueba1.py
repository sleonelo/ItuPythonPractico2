cadena="la arañita de martita"

if any(i=="a" for i in cadena):
    print("no hay una 'z' bro")
    
    
var=input("ingrese A o B: ")
var=var.upper()
print(var)
while var not in ("A","B"):
    var=input("ingrese A o B: ")
