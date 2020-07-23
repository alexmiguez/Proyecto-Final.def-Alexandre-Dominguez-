import numbers
import math
import sys
from tools import ver_otro_barco,lee_numero,rango,numero_valido,lee_entrada,abrir_datos,abrir_json,guardar_datos,agregar_datos,verificar_archivo,esPrimo,esAbundante

class Aplicacion():

    def barco(self,db):
    #'Mostrar los barcos disponibles en base de datos""
        len_db=len(db)
        print(':::::::::')
        print('\nCruceros Disponibles\n')
        for i in range(len_db):
            print(i+1,'.',db[i]['name'])

        opcion=numero_valido(len_db)

        return(opcion)
    
    def destino(self,db):
    #'Mostrar los destinos disponibles en base de datos.Devuelve un destino'
        len_db=len(db)      
        destinos=[]
        print(':::::::::')
        print('\nDestinos Disponibles\n')
        for i in range(len_db):
            destino=db[i]['route']
            for j in range(len(destino)):
                destinos.append(destino[j])

        destinos=list(set(destinos))

        for i in range(len(destinos)):
            print(i+1,'.',destinos[i])

        print('Seleccione un Destino:\n')
        opcion=lee_numero()
        salida=destinos[opcion-1] #la salida es el destino escogido
        return(salida)

    def destino_en_barco(self, db, destino):
    #'Muestra los barcos que pasan por un destino dado'                              
        busqueda=[]                         
        for i in range(len(db)):
            if destino in db[i]['route']:
                busqueda.append(db[i]['name'])
        return(busqueda)
         
    def info_barco(self, opcion,db):
    #'Mostrar la informacion de los barcos'
        print('\nBarco ',db[opcion-1]['name'])  #disponibles en base de datos
        print('\nRuta: \n')
        for i in range(len(db[opcion-1]['route'])):
            print('--->',db[opcion-1]['route'][i])
        
        print('\nFecha de Salida: ', db[opcion-1]['departure'] )
        print('\nPrecio de Boletos: ', db[opcion-1]['cost'] )
        print('\nCapacidad de Habitaciones: ', db[opcion-1]['capacity'] )
        print('\nPiso,Pasillo: ', db[opcion-1]['rooms'])
        
        salida=ver_otro_barco()
        return(salida)

    def tipo_habitacion(self):
    #'Devuelve el tio de habitacion seleccionado'
        print("Seleccione el tipo de Habitacion:\n"
              '1.Simple\n'
              '2.Premium\n'
              '3.VIP\n')
        tipo=numero_valido(3) #mod2=5 #loop para solictar numero correcto de las opciones

        if tipo==1:
            return('simple')
        elif tipo==2:
            return('premium')
        else:
            return('vip')

    def elegir_habitacion(self, opcion, db):
    #'Muestra las habitaciones disponibles en un barco'
        tipos=db[opcion-1]['rooms'] #accede al diccionario 'rooms' del barco seleccionado
        tipo=Aplicacion.tipo_habitacion(self) #Solicita el tipo de habitacion que se mostrará

        capacidad=Aplicacion.capacidad_habitacion(self,db,opcion, tipo)
        id_habitaciones=Aplicacion.id_habitacion(self,tipos, tipo) #Solicta los id del tipo de habitacion seleccionado

        print('\nBarco ',db[opcion-1]['name'])
        print('Habitaciones de clase: ', tipo)
        print('Capacidad de: ',capacidad,' personas')
        print(Aplicacion.servicio_hab(tipo))

        print('ID de habitaciones:\n', id_habitaciones)
        salida=ver_otro_barco()
        return(salida)

    def capacidad_habitacion(self, db,opcion, tipo): #mustra la capacidad de personas en una habitacion
        capac=db[opcion-1]['capacity'][tipo]
        return(capac)

    def servicio_hab(tipo):
    #'Muestra los servicios disponibles para cada tipo de habitacion'
        if tipo=='simple':
            return('Con Servicio de habitacion')
        elif tipo=='premium':
            return('Con Servicio de habitacion y vista al mar')
        elif tipo=='vip':
            return('Con Servicio de habitacion, vista al mar, espacio para fiestas privadas')

    def id_habitacion(self,tipos, tipo):
        #'Crea ID para las habitaciones, dado el tipo (simple, premium o vip)'
        pasillos=tipos[tipo][0] #numero de pasillos del buque y tipo de habitacion seleccionado
        pasillos_id=['A','B','C','D','E','F','G'] #id de pasillos permitidos
        pasillo=pasillos_id[0:pasillos] #id de pasillos del buque y tipo de habitacion seleccionado
        habitaciones=tipos[tipo][1] ##numero de habitaciones del buque y tipo de habitacion seleccionado

        if tipo=='simple':
            id_t='S'
        elif tipo=='premium':
            id_t='P'
        elif tipo=='vip':
            id_t='V'

        habitacion=[]
        for j in pasillo:
            for i in range(habitaciones):
                habitacion.append(id_t+j+str(i+1))
        return(habitacion)

    def selec_habitacion(self, hab, num_personas, capacidad, dato_json, barco):
        #'devuelve el numero de habitaciones a ocupar'
        a=isinstance(dato_json, numbers.Integral) #verifica que el archivo json es nuevo (contiene integer)
        if a is True:
            len_dato=1
        else:
            len_dato=len(dato_json)

        hab_ocup=[]
        for i in range(len_dato):
            if a is True: 
                continue
            elif barco in dato_json[i]["barco"]:
                for j in range(len(dato_json[i]["Habitaciones"][1])):
                    data2=dato_json[i]["Habitaciones"][1][j]
                    hab_ocup.append(data2)

        hab_disp=[]
        for i in range(len(hab)):
            if hab[i] in hab_ocup:
                continue
            else:
                hab_disp.append(hab[i])

        num_hab_disp=len(hab_disp)
        a=num_personas/capacidad #segun el numero de personas
        num_hab=math.ceil(a)     #tambien devuelve el id de las habitaciones          

        if num_hab>num_hab_disp:
            print('Numero de Habitaciones Insuficientes\n'
                  'Seleccione otro tipo de habitación, '
                  'o número menor de pasajeros')
            print('Habitaciones Disponibles: ', num_hab_disp,
                  '\nNúmero máximo de personas: ', num_hab_disp*capacidad)
            main()
        else:
            id_hab=hab_disp[0:num_hab]
            return(num_hab, id_hab)

    def formulario(self, num_personas):
        #'funcion para llenar un formulario con los datos de cada pasajero'
        personas=[]
        for i in range(num_personas):
            nombre=input('Nombre: ')
            print('Documento de identidad')
            doc=lee_numero()
            print('Edad: ')
            edad=lee_numero()
            print('Discapacidad?')
            disc=lee_entrada()

            doc_primo=esPrimo(doc)
            doc_abun=esAbundante(doc)
            upgrade=0

            descuento=0
            if doc_primo is True:
                descuento=descuento+0.1
            if doc_abun is True:
                descuento=descuento+0.15

            if edad>64:
                upgrade=1

            if disc=='SI':
                descuento=descuento+0.3

            personas.append({'Nombre':nombre,'ID':doc,'Edad':edad,'Discapacidad':disc,'Upgrade':upgrade, 'Descuento':descuento})
        return(personas)

    def registro_id(self, opcion_barco, num_personas, asig_habitaciones):
        id_client=str(opcion_barco)+str(num_personas)+str(asig_habitaciones[1][0])
        return(id_client)
        

    def costos(self, datos, barco, tipo_hab, asig_habitaciones, personas):
        #'funcion para calcular el costo total del viaje'
        costo_hab=datos[barco-1]['cost'][tipo_hab]
        num_hab=asig_habitaciones[0]
        monto_total=costo_hab*num_hab
        desc=[]
        for i in range(len(personas)):
            descuentos=personas[i]['Descuento']
            desc.append(descuentos)
            
        desc=sum(desc)
        impuesto=monto_total*0.16
        monto_desc=monto_total-monto_total*desc
        total=monto_desc+impuesto
        costo={'Monto_Total': monto_total, 'Monto_Con_Descuento':monto_desc, 'Impuesto':impuesto,'Total':total}
        return(costo)

    def cliente_a_bordo(self):
        print('¿El pasajero se encuentr a bordo?')
        abordo=lee_entrada()
        return(abordo)

    def buscar(self):
        print('Desea buscar habitacion por:\n'
              '1. Tipo\n2.Capacidad\n3.Id de Habitación',
                '\n4.Volver')
        opcion=numero_valido(4)

        jsonfile='datos.json' # Archivo de almacenamiento de datos
        datos_vacio=None    
        verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
        dato_json=abrir_datos(jsonfile)
        
        if opcion==1:
            encontrado=Aplicacion.buscar_tipo(self,dato_json)
            return(encontrado)
        elif opcion==2:
            encontrado=Aplicacion.buscar_capacidad(self,dato_json)
            return(encontrado)
        elif opcion==3:
            encontrado=Aplicacion.buscar_id(self,dato_json)
            return(encontrado)

    def buscar_tipo(self,dato_json):
        tipo=Aplicacion.tipo_habitacion(self)
        encontrados=[]
        for i in range(len(dato_json)):
            if tipo==dato_json[i]["Tipo Hab"]:
                encontrados.append(dato_json[i])
        return(encontrados)

    def buscar_capacidad(self,dato_json):
        a=lee_numero()
        encontrados=[]
        for i in range(len(dato_json)):
            if a==dato_json[i]["Capacidad Hab"]:
                encontrados.append(dato_json[i])
        return(encontrados)

    def buscar_id(self,dato_json): #Buscar habitacion por ID
        print('\nEscriba el id de la habitacion: ')
        a=input().upper()
        encontrados=[]
        for i in range(len(dato_json)):
            if a in dato_json[i]["Habitaciones"][1]:
                encontrados.append(dato_json[i])
            else:
                pass
                

        if encontrados==[]:
            print('No encontrado')
            encontrados=0
                
        return(encontrados)

    def borrar_registro(self, registro,jsonfile):
        datos=abrir_json(jsonfile)
        for i in range(len(datos)):
            if registro==datos[i]["Boleto_id"]:
                del datos[i]
                break
        print('....\n',datos)     
        return(datos)

    def formulario_tour(self):
        print('Ingrese datos de pasajero')
        nombre=input('Nombre: ')
        print('Documento de identidad')
        doc=lee_numero()
        print('Número de Personas: ')
        num_per=lee_numero()
        formulario={'Nombre':nombre,'ID':doc,'Numero de Personas':num_per}
        return(formulario)
        

    def tour(self, num_per, Num_tour):
        a='Tour en el Puerto'
        b='Degustacion de comida local'
        c='Trotar por el pueblo/ciudad'
        d='Visita a lugares Históricos'
        Num_cli_a=[0]
        Num_cli_b=[0]
        Num_cli_c=[0]
        Num_cli_d=[0]
              
        data=isinstance(Num_tour, numbers.Integral)
        if data is True:
            pass
        else:
            for i in range(len(Num_tour)):
                if Num_tour[i][0]==a:
                    num_cli_a=Num_tour[i][1]
                    Num_cli_a.append(num_cli_a)
                elif Num_tour[i][0]==b:
                    num_cli_b=Num_tour[i][1]
                    Num_cli_b.append(num_cli_b)
                elif Num_tour[i][0]==c:
                    num_cli_c=Num_tour[i][1]
                    Num_cli_c.append(num_cli_c)
                elif Num_tour[i][0]==d:
                    num_cli_d=Num_tour[i][1]
                    Num_cli_d.append(num_cli_d)
        Num_cli_a=sum(Num_cli_a)
        Num_cli_b=sum(Num_cli_b)
        Num_cli_c=sum(Num_cli_c)
        Num_cli_d=sum(Num_cli_d)

        print('Seleecione El Tour\n'
              ' 1.Tour en el Puerto (Vendidos ',Num_cli_a,'/10)\n',
              '2.Degustacion de comida local (Vendidos',Num_cli_b,'/100)\n',
              '3.Trotar por el pueblo/ciudad(sin cupo maximo)\n',
              '4.Visita a lugares Históricos (Vendidos',Num_cli_c,'/15)\n',
              '5.Volver al menu principal')
                     
        opcion=numero_valido(5)
        if opcion==1:
            tour='Tour en el Puerto'
            precio=30
            hora='7 A.M.'
            max_per=4
            cupo_total=10
            disponible=(cupo_total-Num_cli_a)

    
            if num_per>max_per:
                print('Máximo 4 Personas')
                print('\nCupos Disponibles:',disponible)
                #modulo.modulo_3(self)
                
            if num_per>disponible:
                print('Sin cupos sufientes')
                print('\nCupos Disponibles:',disponible,
                  '\nPersonas Maximas:', max_per)
                #modulo.modulo_3(self)
                
            desc=0
            if num_per==3:
                desc=0.1
            if num_per==4:
                desc=0.2

            total=(num_per*precio)-((num_per-2)*precio*desc)
            
  
        elif opcion==2:
            max_per=2
            tour='Degustacion de comida local'
            precio=100
            hora='12 P.M'
            cupo_total=100
            disponible=cupo_total-Num_cli_b
    
            if num_per>max_per:
                print('Máximo 2 Personas')
                print('\nCupos Disponibles:',disponible)
                modulo.modulo_3(self)
            if num_per>disponible:
                print('Sin cupos sufientes')
                print('\nCupos Disponibles:',disponible,
                  '\nPersonas Maximas:', max_per)
                modulo.modulo_3(self)

            
            total=num_per*precio
            
        elif opcion==3:
            tour='Trotar por el pueblo/ciudad'
            precio=0
            max_per=None
            hora='6 A.M.'
            cupo_total=None
            total=0
            
        elif opcion==4:
            tour='Visita a lugares Históricos'
            precio=40
            max_per=4
            hora='10 A.M.'
            cupo_total=15
            disponible=cupo_total-Num_cli_d
            
            if num_per>max_per:
                print('Máximo 4 Personas')
                print('\nCupos Disponibles:',disponible)
                #modulo.modulo_3(self)
            if num_per>disponible:
                print('Sin cupos sufientes')
                print('\nCupos Disponibles:',disponible,
                  '\nPersonas Maximas:', max_per)
                #modulo.modulo_3(self)

            desc=0
            if num_per>2:
                desc=0.1
            
            total=(num_per*precio)-(precio*desc)
            
        elif opcion==5:
            print(".....")
            return 0

        datos_tour={'Tour':tour,'Precio':precio,'MaxPersona':max_per,'Hora':hora,'Cupo Total':cupo_total, 'Total':total}
        return(datos_tour)
