def ingresadatos(p_ventas):
    for i in range(2):

        datos={}
        datos['cuit']=int(input("INGRESE UN CUIT: "))
        datos['rsocial']=input("INGRESE R SOCIAL: ")
        datos['codprod']=int(input("INGRESE CODIGO DE PROD: "))
        datos['monto']=int(input("INGRESE MONTO"))
        p_ventas.append(datos)

ventas=[]
contador=0
ingresadatos(ventas)
cuit=int(input("INGRESE UN CUIT A BUSCAR"))
for i in range(len(ventas)):

    if ventas[i]['cuit']==cuit:
        contador=contador+1

print("Cantidad de vetas del cuit", cuit, " es", contador)

codpro=int(input("INGRESE UN CODIGO DE PRODUCTO A BUSCAR: "))
suma=0
for i in range(len(ventas)):

    if ventas[i]['codprod']==codpro:
        suma=suma+ventas[i]['monto']

print("La suma de ventas para el producto ",codpro," es", suma)