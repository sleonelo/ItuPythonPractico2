ventas=[]
superiores=[]
while True:
    cuit=int(input("ingrese cuit: "))
    r_s=input("ingrese razon social: ")
    c_p=input("ingrese codigo de producto: ")
    m_t=int(input("ingrese el monto total $ "))
    
    
    def dic(cuit,r_s,c_p,m_t):
         vendedor={'cuit': cuit,'rsocial': r_s, 'codprod': c_p, 'montoTotal': m_t}
         ventas.append(vendedor)
         return (ventas)
 
    def superior(ventas):
        for i in range(len(ventas)):
            if ventas[i]['montoTotal']>1000:
                superiores.append(ventas[i]['montoTotal'])
                if len(superiores)>1:
                    del superiores[0]
                    if len(superiores) >2:
                       del superiores[0]
                       del superiores[1]
                
            
        
            print(superiores)
                   
            
        
    dic(cuit,r_s,c_p,m_t)
    superior(ventas)