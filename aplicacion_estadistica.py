import numbers

class estadistica():
    
    def gasto_cliente(self,dato_json1,dato_json2):
        data1=isinstance(dato_json1, numbers.Integral)
        data2=isinstance(dato_json2, numbers.Integral)
        
        clientes=[]
        if data1 is True:
            pass
        else:
            for i in range(len(dato_json1)):
                cliente_principal=dato_json1[i]["Datos de Pasajeros"][0]['Nombre']
                costo=dato_json1[i]["Costos"]["Total"]
                cliente=[cliente_principal, costo]
                clientes.append(cliente)

        clientes2=[]
        if data2 is True:
            pass
        else:
            for i in range(len(dato_json2)):
                cliente_principal=dato_json2[i]["Cliente"]["Nombre"]
                costo=dato_json2[i]["Datos Tour"]["Total"]
                cliente=[cliente_principal, costo]
                clientes2.append(cliente)

        gasto=[]

        if (data1 and data2) is True:
            print('Sin Datos')
            return 0

        elif data1 is True:
            print('Sin Datos de Crucero')
            return clientes2
            
        elif data2 is True:
            print('Sin Datos de Tour')
            return clientes
        
        elif (data1 and data2) is False:
            list_a=[]
            for i in range(len(clientes)):
                for j in range(len(clientes2)):
                    if clientes[i][0] in clientes2[j][0]:
                        gasto_sum=clientes[i][1]+clientes2[j][1]
                        gastos_client=[clientes[i][0],round(gasto_sum,2)]
                        gasto.append(gastos_client)          
            return gasto

    def no_tour(self, dato_json1,dato_json2):
        data1=isinstance(dato_json1, numbers.Integral)
        data2=isinstance(dato_json2, numbers.Integral)
        
        clientes=[]
        if data1 is True:
            pass
        else:
            for i in range(len(dato_json1)):
                cliente_principal=dato_json1[i]["Datos de Pasajeros"][0]['Nombre']
                clientes.append(cliente_principal)

        clientes2=[]
        if data2 is True:
            pass
        else:
            for i in range(len(dato_json2)):
                cliente_principal=dato_json2[i]["Cliente"]["Nombre"]
                clientes2.append(cliente_principal)

        if (data1 and data2) is False:
            list_a=[]
            for i in range(len(clientes)):
                if clientes[i] in clientes2:
                    list_a.append(clientes[i])

            if clientes==[]:
                return ('Sin datos de Pasajeros')

            porcentaje=(1-len(list_a)/len(clientes))*100
            return porcentaje
        
        elif (data1 and data2) is True:
            return ('Sin datos de Pasajeros')
        elif data1 is True:
            return ('Sin datos de Pasajeros')
        else:
            return ('Sin datos de Pasajeros')


    def top(self, gasto):
        
        lista=gasto
        top3=[]
        for i in range(3):
            x, y = zip(*gasto)
            maximo = [[gasto[i],i] for i,a in enumerate(y) if a == max(y)]
            lista.pop(maximo[0][1])
            top3.append(maximo[0][0])
            
        return top3

    def crucero_top(self, dato_json):
        data=isinstance(dato_json, numbers.Integral)
        cruceros=[]
        if data is True:
            print('Sin datos')
            return (0)
        else:
            for i in range(len(dato_json)):
                crucero=dato_json[i]["barco"]
                cruceros.append(crucero)

        cuenta=dict((x,cruceros.count(x)) for x in set(cruceros))
        order=[[k,v] for k, v in sorted(cuenta.items(), key=lambda item:item[1])]
        top=order[::-1]
        
        return top

    def p_vendidos(self, data):

        productos=[]
        cantidad=[]
        for i in range(len(data)):
            for j in range(len(data[i]["sells"])):
                venta=data[i]["sells"][j]["name"]
                cant=data[i]["sells"][j]["amount"]
                
                productos.append(venta)
                cantidad.append([venta,cant])

        cuenta=[[x,productos.count(x)] for x in set(productos)]

        lista=[]
        for i in range(len(cuenta)):
            producto1=cuenta[i][0]
            a=0
            for j in range(len(cantidad)):
                producto2=cantidad[j][0]
                if producto1==producto2:
                    cant=cantidad[j][1]
                    a=cant+a
            lista.append([producto1,a])

        gasto=lista
        top5=[]
        for i in range(5):
            x, y = zip(*lista)
            maximo = [[gasto[i],i] for i,a in enumerate(y) if a == max(y)]
            lista.pop(maximo[0][1])
            top5.append(maximo[0][0])

        return top5
