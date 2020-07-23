#Saman Caribbean
import requests
import sys
import numbers
from matplotlib import pyplot as plt
from tools import ver_otro_barco,lee_numero,rango,numero_valido,lee_entrada,abrir_datos,abrir_json,guardar_datos,agregar_datos,verificar_archivo,esPrimo,esAbundante
from aplicacion import Aplicacion
from aplicacion_rest import Aplicacion_rest
from aplicacion_estadistica import estadistica
#API
##Conectar con base de datos mediante API
response = requests.get('https://saman-caribbean.vercel.app/api/cruise-ships')
print(response)
#convert json to Python object 
data = response.json()


def main():
    #Este es el modulo principal desde donde se accede a los modulos secundarios
    print('\n.......................\nSAMAN CARIBBEAN')
    print('\nBienvenido')
    print('Modulo 1: Gestion de Cruceros \nMódulo 2: Gestion de Habitaciones\n'
          'Modulo 3: Venta de Tour \nModulo 4: Gestion de Restaurante'
          '\nModulo 5: Estadísticas \nPresione 6 para salir')

    opcion=numero_valido(6)
    mod=modulo()
    
    if opcion==1:
        mod.modulo_1()
    elif opcion==2:
        mod.modulo_2()
    elif opcion==3:
        mod.modulo_3()
    elif opcion==4:
        mod.modulo_4()
    elif opcion==5:
        mod.modulo_5()
    else:
        print('Hasta Luego')
        sys.exit()

class modulo():
    def modulo_1(self):
        c=Aplicacion()
        print('\nMódulo 1\n')
        info=''
        while info !='NO':
            opcion=c.barco(data)
            info=c.info_barco(opcion,data)
            if info=='NO':
                main()

    def modulo_2(self):
        c=Aplicacion()
        print('\nMódulo 2\n')
        print('1.Visualizar Habitaciones'
                 '\n2.Vender Habitacion'
                 '\n3.Desocupar Habitacion'
                 '\n4.Buscar Habitacion')

        mod2=numero_valido(4) #solictar numero correcto de las opciones

        if mod2==1: #condicion para entrar en modulo-2:Visualizar Habitaciones
            print('Visualizar Habitaciones')
            info=''
            while info !='NO':
                opcion=c.barco(data)
                info=c.elegir_habitacion(opcion,data)
                if info=='NO':
                    main()

        elif mod2==2: #condicion para entrar en modulo-2:Vender Habitaciones
            jsonfile='datos.json' # Archivo de almacenamiento de datos
            datos_vacio=None    
            verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
            dato_json=abrir_datos(jsonfile)
        
            print('\nVender Habitaciones\n')
            print('Compra de Boletos:\n'
                  '1.Por Destino\n'
                  '2.Por Barco\n'
                  '0. Menú Principal')

            boleto=numero_valido(2)
            if boleto==1:
                destino=c.destino(data)
                print('Destino elegido:', destino)
                barco=c.destino_en_barco(data,destino)
                print('Barcos Disponibles: ', barco)
                print('Seleccione un Barco')
                opcion_barco=c.barco(data)
            elif boleto==2:
                opcion_barco=c.barco(data)
            else:
                main()
                
            barco=data[opcion_barco-1]['name']
            print('Tipo de Habitacion')
            tipo_hab=c.tipo_habitacion()
            print('Numero de Personas')
            num_personas=lee_numero()

            lista_hab=data[opcion_barco-1]['rooms'] #accede a la informacion de habitaciones de un barco desde base de datos principal
            hab=c.id_habitacion(lista_hab, tipo_hab) #se obtiene la identificacion de todas las habitaciones del barco escogido
            capacidad=c.capacidad_habitacion(data, opcion_barco, tipo_hab) #se obtiene la capacidad del tipo de habitacion escogido
            asig_habitaciones=c.selec_habitacion(hab, num_personas, capacidad,dato_json,barco)#se obtiene el numero de habitaciones asignadas al cliente y los id de las habitaciones
            print('capacidad:', capacidad ,'\nnumero:',asig_habitaciones)
            personas=c.formulario(num_personas)
            costo=c.costos(data, opcion_barco, tipo_hab, asig_habitaciones, personas)

            a_bordo=c.cliente_a_bordo()
            registro=c.registro_id(opcion_barco, num_personas, asig_habitaciones)

            datos={'barco':data[opcion_barco-1]['name'],'Tipo Hab':tipo_hab,'Capacidad Hab':capacidad,
                   'Numero de Personas':num_personas,'Habitaciones':asig_habitaciones,
                   'Datos de Pasajeros':personas, 'Costos': costo,
                   'Cliente a Bordo': a_bordo, 'Boleto_id':registro}
            
            print(datos,'\n.................')

            y=agregar_datos(jsonfile, datos)
            guardar_datos(jsonfile, y)
            main()

        elif mod2==3:
            
            jsonfile='datos.json' # Archivo de almacenamiento de datos
            datos_vacio=None    
            verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
            dato_json=abrir_datos(jsonfile)

            print('\nMódulo 3\n')
            print('Desocupar Habitación')
            
            opcion=''
            while opcion!='NO':
                print('Buscar Habitación')
                encontrado=c.buscar_id(dato_json)
                if encontrado==0:
                    print('..............')
                    main()
                print(encontrado)
                registro=input("Escriba el id del boleto: ").upper()

                buscar_boleto=''
                for i in range(len(encontrado)):
                    boleto=encontrado[i]['Boleto_id']
                    if registro==boleto:
                        buscar_boleto=boleto
                        print(buscar_boleto,'...verificado',)

                if buscar_boleto==registro:
                    print('\nDesea Desocupar?')
                    des=lee_entrada()
                    if des=='SI':
                        encontrado[0]['Cliente a Bordo']='NO'
                        dato=c.borrar_registro(registro, jsonfile)
                        dato.append(encontrado[0])
            
                        guardar_datos(jsonfile, dato)
                    print(encontrado)
                    print('\nDesea Buscar Otro?')
                    opcion=lee_entrada()
                    if opcion=='NO':
                        main()
                else:
                    print('Boleto ID no verificado')
                    print('\nDesea Buscar Otro?')
                    opcion=lee_entrada()
                    if opcion=='NO':
                        main()
        
        elif mod2==4:
            print('\nMódulo 4\n')
            opcion=''
            while opcion!='NO':
                print('Buscar Habitación')
                encontrado=c.buscar()
                print(encontrado)
                
                print('\nDesea Buscar Otro?')
                opcion=lee_entrada()
                if opcion=='NO':
                    main()
                    
    def modulo_3(self):
        c=Aplicacion()
        jsonfile='datos_tour.json' # Archivo de almacenamiento de datos
        datos_vacio=None    
        verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json=abrir_datos(jsonfile)

        Num_tour=[]
        dato_true=isinstance(dato_json, numbers.Integral)
        if dato_true is True:
            pass
        else:
            for i in range(len(dato_json)):
                num_cli=dato_json[i]['Cliente']['Numero de Personas']
                num_tour=dato_json[i]['Datos Tour']['Tour']
                Num_tour.append([num_tour,num_cli])
            
        opcion=''
        while opcion!='NO':
            print('......................\n'
                '\n   Modulo 3\n'
                  'Venta de Tour\n')
            formulario=c.formulario_tour()
            tour_barco=c.tour(formulario['Numero de Personas'], Num_tour)
            if tour_barco==0:
                main()

            dato={'Cliente':formulario, 'Datos Tour':tour_barco}

            y=agregar_datos(jsonfile, dato)
            guardar_datos(jsonfile, y)

            print(dato)

            print('\nDesea Agregar Otro?')
            opcion=lee_entrada()
            if opcion=='NO':
                main()

    def modulo_4(self):
        d=Aplicacion_rest()
        print('\nModulo 4'
              '\nGestion de Restaurante\n')
        jsonfile='datos_rest.json' # Archivo de almacenamiento de datos
        datos_vacio=None    
        verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json=abrir_datos(jsonfile)

        opcion=''
        while opcion!='NO':
            print('.........................................\n'
                'GESTION DE RESTAURANTE\n'
                '\nSeleccione Opcion\n'
                  '1.Buscar Producto o Combo \n'
                  '2.Agregar Producto\n'
                  '3.Eliminar Producto \n'
                  '4.Modificar Producto\n'
                  '5.Agregar Combo \n'
                  '6.Eliminar Combo \n'
                  '7.Modificar Combo \n'
                  '8.Ir al Menú Principal')
            menu=numero_valido(8)
            
            if menu==1:
                print('Buscar Producto o Combo?')
                clase=d.lee_clase()
                resultado=d.buscar_rest(dato_json,clase)
                if resultado==0:
                    main()
                    
                print(resultado)
                
            elif menu==2:
                print('Agregar Producto')
                producto=d.agregar()
                print(producto)
                y=agregar_datos(jsonfile, producto)
                guardar_datos(jsonfile, y)
                main()
       
            elif menu==3:
                print('Eliminar Producto')
                clase='P'
                eliminar=d.eliminar_prod_comb(dato_json, clase)

                if eliminar==0:
                    print('No encontrado')
                    main()
                if eliminar=='No encontrado':
                    print('No encontrado')
                    main()
                
                guardar_datos(jsonfile, eliminar)
                main()

            elif menu==4:
                print('Modificar Producto')
                clase='P'
                print('Buscar Producto')
                resultado=d.buscar_rest(dato_json,clase)
                print(resultado)
                if resultado=='No encontrado':
                    main()
                if resultado=='Sin datos':
                    main()
                
                id_colect=resultado[0]['cod']
                print('Desea Modificar?')
                opcion=lee_entrada()
                if opcion=='SI':
                    producto=d.agregar()
                    eliminar=d.eliminar_prod(dato_json, clase, id_colect)
                    guardar_datos(jsonfile, eliminar)
                    y=agregar_datos(jsonfile, producto)
                    guardar_datos(jsonfile, y)
                else:
                    main()
                
            elif menu==5:
                print('Agregar Combo')
                combo=d.agregar_combo()
                print(combo)
                y=agregar_datos(jsonfile, combo)
                guardar_datos(jsonfile, y)
                main()

                
            elif menu==6:
                print('Eliminar Combo')
                clase='C'
                eliminar=d.eliminar_prod_comb(dato_json, clase)

                if eliminar==0:
                    print('No encontrado')
                    main()
                if eliminar=='No encontrado':
                    print('No encontrado')
                    main()
                
                guardar_datos(jsonfile, eliminar)
                main()
                
                
            elif menu==7:
                print('Modificar Combo')
                clase='C'
                print('Buscar Producto')
                resultado=d.buscar_rest(dato_json,clase)
                print(resultado)
                if resultado=='No encontrado':
                    main()
                if resultado=='Sin datos':
                    main()


                
                id_colect=resultado[0]['cod']
                print('Desea Modificar?')
                opcion=lee_entrada()
                if opcion=='SI':
                    producto=d.agregar_combo()
                    eliminar=d.eliminar_prod(dato_json, clase, id_colect)
                    guardar_datos(jsonfile, eliminar)
                    y=agregar_datos(jsonfile, producto)
                    guardar_datos(jsonfile, y)
                else:
                    main()               
                
            elif menu==8:
                print('..............')
                main()

            print('\nCotinuar en Gestion de Restaurant?')
            opcion=lee_entrada()
            if opcion=='NO':
                main()

    def modulo_5(self):
        a=estadistica()

        jsonfile1='datos.json' # Archivo de almacenamiento de datos
        jsonfile2='datos_tour.json'

        datos_vacio=None    
        verificar_archivo(jsonfile1,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json1=abrir_datos(jsonfile1)

        verificar_archivo(jsonfile2,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json2=abrir_datos(jsonfile2)

        print('..................................')

        print('\nModulo 5'
              '\Estadísticas')
        print('\n1.Gasto por cliente (Ticket+Tour)'
              '\n2.Porcentaje de Clientes que no Compran Tour'
              '\n3.Clientes (primeros 3)de mayor fidelidad (que gastan más dinero)'
              '\n4.Top 3 Cruceros con más ventas en Tickets'
              '\n5.Top 5 Productos más vendidos en Restaurant'
              '\n6. Volver al menú principal')
        menu=numero_valido(6)

        if menu==1:
            print('\nPromedio de gasto de un cliente en el crucero  (Ticket+Tour)')
            gasto=a.gasto_cliente(dato_json1,dato_json2)
            if gasto==0:
                print('\n..................................')
                modulo.modulo_5(self)
                
            monto=[]
            for i in range(len(gasto)):
                monto_cliente=gasto[i][1]
                monto.append(monto_cliente)

            personas=[]
            for i in range(len(gasto)):
                persona_cliente=gasto[i][0]
                personas.append(persona_cliente)

            monto_suma=sum(monto)
            promedio=monto_suma/len(gasto)
            print('Promedio de Gasto: ',round(promedio,2))
            print('\n..................................')
            modulo.modulo_5(self)
            
        elif menu==2:
            print('\nPorcentaje de Clientes que no Compran Tour')
            notour=a.no_tour(dato_json1,dato_json2)
            
            if notour=='Sin datos de Pasajeros':
                print(notour)
                print('\n..................................')
                pass
            else:
                sitour=100-notour
                print(str(round(notour,1))+'%')
                print('\n..................................')
                #Grafico
                fig=plt.figure()
                ax=fig.add_axes([0,0,1,1])
                ax.axis('equal')
                langs=['Si compran Tour','No compran Tour']
                pct=[sitour,notour]
                ax.pie(pct, labels=langs,autopct='%1.2f%%')
                ax.set_title('Porcentaje de Clientes que no Compran Tour')
                plt.show()


            modulo.modulo_5(self)
            
        elif menu==3:
            print('\nClientes (primeros 3)de mayor fidelidad')
            gasto=a.gasto_cliente(dato_json1,dato_json2)
            if gasto==0:
                print('\n..................................')
                modulo.modulo_5(self)

       
            top3=a.top(gasto)
           
            for i in range(len(top3)):
                print(i+1,'.Nombre: ',top3[i][0],'   Monto: ',top3[i][1])
             

            print('\n..................................')
    

            modulo.modulo_5(self)
        
        elif menu==4:
            print('\nTop 3 Cruceros con más ventas en Tickets')
            crtop=a.crucero_top(dato_json1)

            if crtop==0:
                print('Sin datos de Pasajeros')
                print('\n..................................')
                modulo.modulo_5(self)
            else:    
                for i in range(3):
                    print(i+1,'.Crucero: ',crtop[i][0],'   Tickets:',crtop[i][1])
                print('\n..................................')
                modulo.modulo_5(self)
                
        elif menu==5:
            print('\nTop 5 Productos más vendidos en Restaurant')
            venta=a.p_vendidos(data)

            langs=[]
            pct=[]
            for i in range(5):
                print(i+1,'...',venta[i][0],'   Ventas:',venta[i][1])
                langs.append(venta[i][0])
                pct.append(venta[i][1])
            print('\n..................................')
            
            fig=plt.figure()
            ax=fig.add_axes([0,0,1,1])
            ax.axis('equal') 
            ax.pie(pct, labels=langs,autopct='%1.2f%%')
            ax.set_title('Top 5 Productos más vendidos en Restaurant')
            plt.show()

            modulo.modulo_5(self)
            
        elif menu==6:
            main()

main()
