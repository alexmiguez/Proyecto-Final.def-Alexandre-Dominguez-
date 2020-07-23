# Proyecto-Final.def-Alexandre-Dominguez-
README

El programa inicia con main.py. Allí se muestra la interfaz principal, y desde este archivo de accede a todos los modulos.
 
Los datos se descargan con API. y se guardan en una lista (data), que contiene todos los diccionarios con la informacion de cada crucero.

El progrma funciona con los siguientes archivos:

-Main
----aplicacion
----aplicacion_rest
----aplicacion_estadistica
----tools

En aplicacion se administra la informacion de pasajeros del barco.
En aplicacion_rest se administra la informacion del restaurante.
En aplicacion estadística, se administran los datos del barco y restaurante.
tools es un archivo auxiliar, con funciones para administrar datos de entrada y salida. 

------------------------MODULOS----------------
Módulo1
En el primer modulo se accede a data, y se muestran todas las especificaciones de los barcos. 

Módulo 2
En el modulo 2, se administra la visualizacion y disponibilidad de las habitaciones. Se accede al archivo aplicacion.py y a data (archivos descargados con API). 

Los datos creados en módulo 2 se guardan en un archivo json (de nombre datos.json). Si tal archivo no existe, automaticamente se crea uno nuevo. Si existe, entonces puede modificarse.

El modúlo asigna automaticamente habitaciones diferentes (dependiendo del numero de personas) a cada "pasajero principal" que compre un boleto, y del que se guarda informacion.  Si el pasajero abandona el barco, se conservan los datos y se modifica el estatus de "cliente a bordo".

Módulo 3
Se accede al archivo aplicacion.py y a data (archivos descargados con API). 

En el modulo 3, se administra la venta de tour. Los datos creados en módulo 3 se guardan en un archivo json (de nombre datos_tour.json). Si tal archivo no existe, automaticamente se crea uno nuevo. Si existe, entonces puede modificarse.

Este modulo contabiliza la disponibilidad de personas por tour.

Módulo 4
Se accede al archivo aplicacion_rest.py y a data (archivos descargados con API). 

En el modulo 4, se administra el almacenamiento de alimentos y bebidas, del restaurante de un barco.

Los datos creados en módulo 4 se guardan en un archivo json (de nombre datos_rest.json). Si tal archivo no existe, automaticamente se crea uno nuevo. Si existe, entonces puede modificarse.

Módulo 5
Se accede al archivo aplicacion_estadistica.py y a data (archivos descargados con API). También accede a los archivos datos.json y datos_tour. Si tales archivos no existen, automaticamente se crean de nuevo.

En el módulo 5 se muestran algunas estadísticas de los pasajeros, venta de tour y restaurant.

