import numbers
from tools import ver_otro_barco,lee_numero,rango,numero_valido,lee_entrada,abrir_datos,abrir_json,guardar_datos,agregar_datos,verificar_archivo,esPrimo,esAbundante
class Aplicacion_rest():
#'Apliccion secundaria que controla las opciones sobre un restaurant'
    
    def agregar(self):
        nombre=input('Nombre de Alimento o Bebida :')
        print('Clasificacion (alimento/bebida)')
        clasif=Aplicacion_rest.lee_clasificacion(self)
        if clasif=='A':
            tipo=Aplicacion_rest.lee_clas_A(self)
        elif clasif=='B':
            tipo=Aplicacion_rest.lee_clas_B(self)
        print('Ingrese el precio')
        precio=lee_numero()
        precio=precio+precio*.16

        cod_id='P'+nombre+clasif+tipo
        alimento={'CLASE':'P','Nombre':nombre,'Clasificacion':clasif,'Tipo':tipo,'Precio':precio,'cod':cod_id}
        return(alimento)

    def agregar_combo(self):
        nombre=input('Nombre del Combo')
        num_prod=0
        productos=[]
        opcion=''
        while opcion!='NO':

            producto=input('Agregue un producto')
            productos.append(producto)
            num_prod=num_prod+1

            if num_prod<2:
                print('Agregue Otro')
                continue
            else:
                print('\nAgregar otro producto?')
                opcion=lee_entrada()
                if opcion=='NO':
                    break
        print('Indique precio del combo')
        precio_a=lee_numero()
        precio=precio_a+precio_a*.16
        cod_id='C'+nombre+str(precio_a)

        combo={'CLASE':'C', 'Nombre':nombre, 'Productos': productos, 'Precio':precio,'cod':cod_id }
        return(combo)

    def lee_clase(self):
    #'funcion para pedir al usuario una clasificacion de alimento/bebida'
    #'devuelve los carateres  alimento o bebida, en mayusculas'
        while True: 
            print("Ingrese P (producto) o C (combo)")
            opcion = input().upper()
            if opcion in ["P", "C"]:
                return opcion
            
    def lee_clasificacion(self):
    #'funcion para pedir al usuario una clasificacion de alimento/bebida'
    #'devuelve los carateres  alimento o bebida, en mayusculas'
        while True: 
            print("Ingrese A (Alimento) o B (bebida)")
            opcion = input().upper()
            if opcion in ["A", "B"]:
                return opcion
            
    def lee_clas_A(self):
    #'funcion para pedir al usuario una clasificacion de alimento'
        while True: 
            print("Ingrese E (empaque) o P (preparacion)")
            opcion = input().upper()
            if opcion in ["E", "P"]:
                return opcion
            
    def lee_clas_B(self):
    #'funcion para pedir al usuario una clasificacion de bebida''
        while True: 
            print("Ingrese S (prqueño), M (mediano) o G (grande)")
            opcion = input().upper()
            if opcion in ["S", "M", "G"]:
                return (opcion)

    def buscar_rest(self, dato_json, clase):
        print('\nBuscar por:\n'
            '1.Nombre\n'
            '2.Rango de Precio\n'
            '3.Volver')
        buscar_op=numero_valido(3)
        
        if buscar_op==1:
          resultado=Aplicacion_rest.buscar_nombre_rest(self,dato_json, clase)
        elif buscar_op==2:
          resultado=Aplicacion_rest.buscar_rango_rest(self,dato_json, clase)
        elif buscar_op==3:
            resultado=0

        if resultado==[]:
            resultado='No encontrado'
          
        return resultado
      
    def buscar_nombre_rest(self, dato_json, clase):
        print('Buscar por nombre')
        nombre=input('Nombre: ')

        if dato_json==None:
            return 0

        data=isinstance(dato_json, numbers.Integral)
        if data is True:
            Resultado='Sin datos'

        else:
            Resultado=[]
            for i in range(len(dato_json)):
                if clase==dato_json[i]['CLASE']:
                    if nombre in dato_json[i]['Nombre']:
                        resultado=dato_json[i]
                        Resultado.append(resultado)

        return(Resultado)
        
    def buscar_rango_rest(self, dato_json, clase):
        rango_val=rango()
        rango_min=rango_val[0]
        rango_max=rango_val[1]

        if dato_json==None:
            return 0
        
        data=isinstance(dato_json, numbers.Integral)
        if data is True:
            Resultado='Sin datos'
            
        else:
            Resultado=[]
            for i in range(len(dato_json)):
                if clase==dato_json[i]['CLASE']:
                    if (dato_json[i]['Precio']>=rango_min and dato_json[i]['Precio']<=rango_max):
                        resultado=dato_json[i]
                        Resultado.append(resultado)
        return(Resultado)

    def eliminar_prod_comb(self, dato_json, clase):
        
        buscar=Aplicacion_rest.buscar_rest(self, dato_json, clase)

        if buscar==0:
            return 0
        if buscar=='Sin datos':
            return 0

        colect=[]
        id_colect=[]
        
        dat=isinstance(buscar, numbers.Integral)
        
        if dat is True:
            print('Sin datos')
            return 0
        else:
            for i in range(len(buscar)):
                if clase==buscar[i]["CLASE"]:
                    colect.append(buscar[i])
                    id_colect.append(buscar[i]['cod'])
                
        data=isinstance(colect, numbers.Integral)
        if data is True:
            print('Sin datos')
            main()
        else:
            print('Reultados:\n',colect)
            print('Desea Eliminar?')
            opcion=lee_entrada()
            if opcion=='SI':
                for i in range(len(dato_json)):
                    if dato_json[i]["cod"] in id_colect:
                        print('ID: ',id_colect)
                        del dato_json[i]
                        print('....\n',dato_json)
                        return(dato_json)
