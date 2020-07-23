import json
import os
import numbers
def ver_otro_barco():
    #'pregunta al usuario si desea repetir el proceso de visualizar un barco'
    print('\nDesea ver otro barco?\n')
    salida=lee_entrada()
    return(salida)

def lee_numero():
    #'Se pide un valor entero y lo devuelve.'
    #'Mientras el valor ingresado no sea entero, vuelve a solicitarlo'
    while True:
        valor = input("\nIngrese número\n")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero sin decimales .")

def rango():
    while True:
        print("\nIngrese número minimo\n")
        valor_min=lee_numero()
        print("\nIngrese número maximo\n")
        valor_max=lee_numero()
        if valor_max>valor_min:
            return([valor_min,valor_max])
        else:
            print("Error. Introduzca de Nuevo el Rango")

def numero_valido(numero_max):
    #'devuelve un numero válido dado una serie de opciones numeradas'
    opcion=numero_max+1
    while opcion>numero_max:
        opcion=lee_numero()
        print('\n')
        if opcion>numero_max:
            print('Ingrese un numero válido')
    return(opcion)
    
def lee_entrada():
    #'funcion para pedir al usuario si desea realizar accion'
    #'devuelve los carateres  SI O NO, en mayusculas'
        while True: 
            print("Ingrese SI o NO")
            opcion = input().upper()
            if opcion in ["SI", "NO"]:
                return opcion

def abrir_datos(jsonfile):
    #'funcion para leer un archivo json'
    f=open(jsonfile)
    print(f)
    dato=json.load(f)
    return(dato)

def abrir_json(jsonfile):
    #funcion para leer datos de json y convertirlos en lista
    #jsonfile='datos.json' # Archivo de almacenamiento de datos
    datos_vacio=None    
    verificar_archivo(jsonfile,datos_vacio) #verificar la existencia del archivo json, o creacion de uno
    dato_json=abrir_datos(jsonfile)
    return(dato_json)
    
def guardar_datos(jsonfile, datos):
    #'funcion para guardar un archivo json'
    with open(jsonfile, 'w') as f:
        json.dump(datos, f)

def agregar_datos(jsonfile, datos):
    #'funcion para agregar datos a un archivo json'
    dato=abrir_datos(jsonfile)
    
    data=isinstance(dato, numbers.Integral)
    if data is True:
        dato=[datos]
    else:
        dato.append(datos)
    return(dato)

def verificar_archivo(archivo, datos):
    #'funcion para verificar la existencia de un archivo json'
    if os.path.isfile(archivo) and os.access(archivo, os.R_OK):
        print ("Base de Datos Verificada\n")
    else:
        print ("No se encontró base de datos\nCreando archivo json...")
        guardar_datos(archivo, 0)
        
def esPrimo(num):
    #'funcion para saber si un numero es primo'
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def esAbundante(num):
    #'funcion para saber si un numero es abundante'
    count =  1
    suma = 0
    while (count<num):
      if (num%count==0):
        suma+=count
      count = count + 1
    
    if (suma>(num)):
      return True
    else:
      return False
